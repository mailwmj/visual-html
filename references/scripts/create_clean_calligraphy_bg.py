from pathlib import Path
from PIL import Image
import numpy as np

def make_perfect_calligraphy_bg():
    assets_dir = Path(__file__).resolve().parents[1] / 'styles' / 'ink-calligraphy' / 'assets'
    assets_dir.mkdir(parents=True, exist_ok=True)

    p1 = r'C:\Users\mailwmj\.gemini\antigravity\brain\222781ed-da9e-4964-814c-14f36b75b0e4\.user_uploaded\media_1787757924368.png'
    p2 = r'C:\Users\mailwmj\.gemini\antigravity\brain\222781ed-da9e-4964-814c-14f36b75b0e4\.user_uploaded\media_1787758134583.png'

    im1 = Image.open(p1).convert('RGBA') # "蓬莱" with dry brush
    im2 = Image.open(p2).convert('RGBA') # "三国" with ink splatters

    width, height = 2560, 1440
    # Base warm raw Xuan paper: #F5F2EB
    bg = Image.new('RGB', (width, height), (245, 242, 235))
    bg_arr = np.array(bg, dtype=np.float32)

    # 1. Mulberry paper grain
    np.random.seed(42)
    grain = np.random.normal(0, 1.8, (height, width, 3))
    bg_arr = np.clip(bg_arr + grain, 0, 255).astype(np.uint8)
    bg = Image.fromarray(bg_arr, mode='RGB').convert('RGBA')

    # 2. Process im1 ("蓬莱" master dry brush strokes)
    arr1 = np.array(im1, dtype=np.float32)
    lum1 = 0.299 * arr1[:, :, 0] + 0.587 * arr1[:, :, 1] + 0.114 * arr1[:, :, 2]
    paper_lum = 232.0
    ink_mask1 = np.clip((paper_lum - lum1) / 185.0, 0.0, 1.0)
    ink_mask1 = np.power(ink_mask1, 1.1)

    stroke_r = np.full_like(lum1, 20.0)
    stroke_g = np.full_like(lum1, 19.0)
    stroke_b = np.full_like(lum1, 18.0)
    stroke_a = ink_mask1 * 255.0

    red_diff = arr1[:, :, 0] - np.maximum(arr1[:, :, 1], arr1[:, :, 2])
    is_seal = (red_diff > 25.0) & (arr1[:, :, 0] > 120.0)
    stroke_r[is_seal] = 194.0 # #C23531
    stroke_g[is_seal] = 53.0
    stroke_b[is_seal] = 49.0
    stroke_a[is_seal] = np.clip(red_diff[is_seal] / 80.0, 0.2, 1.0) * 255.0

    clean_stroke1 = Image.fromarray(np.stack([stroke_r, stroke_g, stroke_b, stroke_a], axis=2).astype(np.uint8), mode='RGBA')

    # 3. Process im2 ("三国" ink splatters & bold calligraphy)
    arr2 = np.array(im2, dtype=np.float32)
    lum2 = 0.299 * arr2[:, :, 0] + 0.587 * arr2[:, :, 1] + 0.114 * arr2[:, :, 2]
    paper_lum2 = 240.0
    ink_mask2 = np.clip((paper_lum2 - lum2) / 190.0, 0.0, 1.0)
    ink_mask2 = np.power(ink_mask2, 1.1)

    stroke_r2 = np.full_like(lum2, 20.0)
    stroke_g2 = np.full_like(lum2, 19.0)
    stroke_b2 = np.full_like(lum2, 18.0)
    stroke_a2 = ink_mask2 * 255.0

    red_diff2 = arr2[:, :, 0] - np.maximum(arr2[:, :, 1], arr2[:, :, 2])
    is_seal2 = (red_diff2 > 25.0) & (arr2[:, :, 0] > 120.0)
    stroke_r2[is_seal2] = 194.0
    stroke_g2[is_seal2] = 53.0
    stroke_b2[is_seal2] = 49.0
    stroke_a2[is_seal2] = np.clip(red_diff2[is_seal2] / 80.0, 0.2, 1.0) * 255.0

    clean_stroke2 = Image.fromarray(np.stack([stroke_r2, stroke_g2, stroke_b2, stroke_a2], axis=2).astype(np.uint8), mode='RGBA')

    # 4. Composite onto canvas:
    # Right flank: Large sweeping calligraphy with feibai extending from x = 1750 to 2550
    w1 = 1100
    h1 = int(w1 * clean_stroke1.height / clean_stroke1.width)
    s1_placed = clean_stroke1.resize((w1, h1), Image.Resampling.LANCZOS)
    s1_arr = np.array(s1_placed, dtype=np.float32)
    s1_arr[:, :, 3] = s1_arr[:, :, 3] * 0.48 # 48% clear visibility
    s1_faded = Image.fromarray(s1_arr.astype(np.uint8), mode='RGBA')
    bg.paste(s1_faded, (width - w1 + 180, 20), s1_faded)

    # Left flank: Sweeping calligraphy & splatters from x = -60 to 700
    w2 = 900
    h2 = int(w2 * clean_stroke2.height / clean_stroke2.width)
    s2_placed = clean_stroke2.resize((w2, h2), Image.Resampling.LANCZOS)
    s2_arr = np.array(s2_placed, dtype=np.float32)
    s2_arr[:, :, 3] = s2_arr[:, :, 3] * 0.42 # 42% visibility
    s2_faded = Image.fromarray(s2_arr.astype(np.uint8), mode='RGBA')
    bg.paste(s2_faded, (-40, height - h2 + 20), s2_faded)

    # Top-left subtle ink splatters
    w_sp = 600
    h_sp = int(w_sp * clean_stroke2.height / clean_stroke2.width)
    sp_placed = clean_stroke2.resize((w_sp, h_sp), Image.Resampling.LANCZOS)
    sp_arr = np.array(sp_placed, dtype=np.float32)
    sp_arr[:, :, 3] = sp_arr[:, :, 3] * 0.28
    sp_faded = Image.fromarray(sp_arr.astype(np.uint8), mode='RGBA')
    bg.paste(sp_faded, (-100, -30), sp_faded)

    # Save
    final_bg = bg.convert('RGB')
    bg_jpg_path = assets_dir / "calligraphy-bg.jpg"
    final_bg.save(bg_jpg_path, format="JPEG", quality=93, optimize=True)
    print(f"Generated {bg_jpg_path} ({bg_jpg_path.stat().st_size // 1024} KB)")

if __name__ == '__main__':
    make_perfect_calligraphy_bg()
