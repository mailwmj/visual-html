#!/usr/bin/env python3
"""Regression tests for the hybrid and strict offline HTML bundler."""

from __future__ import annotations

import base64
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "references" / "scripts" / "bundle_offline.py"
SPEC = importlib.util.spec_from_file_location("bundle_offline", SCRIPT_PATH)
assert SPEC and SPEC.loader
bundle_offline = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle_offline)


PNG_HEADER = b"\x89PNG\r\n\x1a\n" + b"offline-test"


class BundleOfflineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "styles.css").write_text(
            ".hero { background-image: url('texture.bin'); }", encoding="utf-8"
        )
        (self.root / "texture.bin").write_bytes(b"local texture")
        (self.root / "asset.png").write_bytes(PNG_HEADER)
        self.input_path = self.root / "page.html"
        self.input_path.write_text(
            """<!doctype html>
<html><head>
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">
  <style>.remote { background: url('//cdn.example.test/remote.png'); }</style>
</head><body>
  <img src="asset.png" alt="asset">
  <pre class="mermaid">flowchart LR
    A[Input] -->|ready| B[Output]
  </pre>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true });
  </script>
</body></html>""",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_hybrid_keeps_online_enhancements_and_static_fallback(self) -> None:
        output_path = self.root / "hybrid.html"

        bundle_offline.bundle(self.input_path, output_path, strict=False, font_map=None, check=False)
        output = output_path.read_text(encoding="utf-8")

        self.assertIn('class="mermaid-static"', output)
        self.assertIn("mermaid-source", output)
        self.assertIn(bundle_offline.MERMAID_IMPORT, output)
        self.assertIn("fonts.googleapis.com", output)
        self.assertIn("data:image/png;base64,", output)
        stylesheet = re.search(r'href="data:text/css;base64,([^"]+)"', output)
        self.assertIsNotNone(stylesheet)
        decoded_stylesheet = base64.b64decode(stylesheet.group(1)).decode("utf-8")
        self.assertIn("data:application/octet-stream;base64,", decoded_stylesheet)

    def test_strict_removes_external_enhancements(self) -> None:
        output_path = self.root / "strict.html"
        strict_input = self.root / "strict-input.html"
        strict_input.write_text(
            self.input_path.read_text(encoding="utf-8").replace(
                "url('//cdn.example.test/remote.png')", "url('texture.bin')"
            ),
            encoding="utf-8",
        )

        bundle_offline.bundle(strict_input, output_path, strict=True, font_map=None, check=False)
        output = output_path.read_text(encoding="utf-8")

        self.assertIn('content="strict-v1"', output)
        self.assertIn('class="mermaid-static"', output)
        self.assertNotIn(bundle_offline.MERMAID_IMPORT, output)
        self.assertNotIn("fonts.googleapis.com", output)
        self.assertNotIn("cdn.example.test", output)
        self.assertNotIn('src="asset.png"', output)
        self.assertIn("data:image/png;base64,", output)

    def test_strict_rejects_protocol_relative_external_resources(self) -> None:
        with self.assertRaisesRegex(ValueError, "external CSS resource remains"):
            bundle_offline.bundle(self.input_path, None, strict=True, font_map=None, check=True)

    def test_strict_rejects_bare_external_css_imports(self) -> None:
        imported = self.root / "imported.html"
        imported.write_text(
            '<style>@import "https://cdn.example.test/theme.css";</style>', encoding="utf-8"
        )

        with self.assertRaisesRegex(ValueError, "external CSS resource remains"):
            bundle_offline.bundle(imported, None, strict=True, font_map=None, check=True)

    def test_strict_rejects_missing_local_resources(self) -> None:
        missing = self.root / "missing.html"
        missing.write_text('<img src="does-not-exist.png">', encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "missing local resource"):
            bundle_offline.bundle(missing, None, strict=True, font_map=None, check=True)

    def test_font_map_embeds_requested_font(self) -> None:
        font_dir = self.root / "fonts"
        font_dir.mkdir()
        (font_dir / "Brand.woff2").write_bytes(b"font-bytes")
        font_map = self.root / "fonts.json"
        font_map.write_text(
            json.dumps({"Brand Sans": [{"path": "fonts/Brand.woff2", "weight": 600}]}),
            encoding="utf-8",
        )
        output_path = self.root / "font-map.html"

        bundle_offline.bundle(self.input_path, output_path, strict=False, font_map=font_map, check=False)
        output = output_path.read_text(encoding="utf-8")

        self.assertIn("@font-face", output)
        self.assertIn('font-family: "Brand Sans"', output)
        self.assertIn("data:font/woff2;base64,", output)

    def test_fallback_preserves_labels_and_edge_labels(self) -> None:
        output_path = self.root / "labels.html"
        strict_input = self.root / "labels-input.html"
        strict_input.write_text(
            self.input_path.read_text(encoding="utf-8").replace(
                "url('//cdn.example.test/remote.png')", "url('texture.bin')"
            ),
            encoding="utf-8",
        )

        bundle_offline.bundle(strict_input, output_path, strict=True, font_map=None, check=False)
        output = output_path.read_text(encoding="utf-8")

        self.assertIn("Input", output)
        self.assertIn("Output", output)
        self.assertIn("ready", output)
        self.assertIn('role="img"', output)


if __name__ == "__main__":
    unittest.main()
