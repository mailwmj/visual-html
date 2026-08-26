import os
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np

def extract_ink_alpha(img_path, threshold_low=0.20, threshold_high=0.90):
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img, dtype=np.float32) / 255.0
    
    # Calculate luminance
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    
    # Alpha curve
    alpha = np.clip((threshold_high - lum) / (threshold_high - threshold_low), 0.0, 1.0)
    alpha = np.power(alpha, 1.15) * 255.0
    
    # Base dark ink color
    r = np.full_like(lum, 18.0)
    g = np.full_like(lum, 17.0)
    b = np.full_like(lum, 16.0)
    
    # Preserve red seals
    redness = arr[:, :, 0] - (arr[:, :, 1] + arr[:, :, 2]) * 0.5
    is_seal = redness > 0.12
    r[is_seal] = arr[:, :, 0][is_seal] * 255.0
    g[is_seal] = arr[:, :, 1][is_seal] * 255.0
    b[is_seal] = arr[:, :, 2][is_seal] * 255.0
    alpha[is_seal] = np.clip(redness[is_seal] * 3.5, 0.0, 1.0) * 255.0
    
    rgba_arr = np.stack([r, g, b, alpha], axis=2).astype(np.uint8)
    return Image.fromarray(rgba_arr, mode='RGBA')

def create_master_calligraphy_bg(assets_dir, user_img1, user_img2):
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    stroke1 = extract_ink_alpha(user_img1, threshold_low=0.18, threshold_high=0.88)
    stroke2 = extract_ink_alpha(user_img2, threshold_low=0.22, threshold_high=0.88)
    
    width, height = 2560, 1440
    bg = Image.new('RGBA', (width, height), (245, 242, 235, 255)) # #F5F2EB
    
    bg_arr = np.array(bg, dtype=np.float32)
    y_coords, x_coords = np.mgrid[0:height, 0:width]
    
    # Subtle ambient lighting
    dist_tr = np.sqrt(((x_coords - width) / width)**2 + (y_coords / height)**2)
    warm_tint = np.clip(1.0 - dist_tr * 1.1, 0.0, 1.0)
    bg_arr[:, :, 0] += warm_tint * 5.0
    bg_arr[:, :, 1] += warm_tint * 3.0
    bg_arr[:, :, 2] += warm_tint * 1.0
    
    # Mulberry raw paper texture
    np.random.seed(42)
    noise = np.random.normal(0, 2.2, (height, width, 3))
    bg_arr[:, :, :3] = np.clip(bg_arr[:, :, :3] + noise, 0, 255)
    bg = Image.fromarray(bg_arr.astype(np.uint8), mode='RGBA')
    
    # 1. Master Calligraphy Artwork on the Right Side (Expansive & Atmospheric)
    s1_w = int(width * 0.42)
    s1_h = int(s1_w * stroke1.height / stroke1.width)
    s1_large = stroke1.resize((s1_w, s1_h), Image.Resampling.LANCZOS)
    
    s1_arr = np.array(s1_large, dtype=np.float32)
    s1_arr[:, :, 3] = s1_arr[:, :, 3] * 0.32 # 32% elegant atmospheric opacity
    s1_layer = Image.fromarray(s1_arr.astype(np.uint8), mode='RGBA')
    
    # Paste on right side
    bg.paste(s1_layer, (width - s1_w + 80, int(height * 0.08)), s1_layer)
    
    # 2. Dynamic Ink Splatter Cluster on Left & Lower Canvas
    s2_w = int(width * 0.32)
    s2_h = int(s2_w * stroke2.height / stroke2.width)
    s2_large = stroke2.resize((s2_w, s2_h), Image.Resampling.LANCZOS)
    
    s2_arr = np.array(s2_large, dtype=np.float32)
    s2_arr[:, :, 3] = s2_arr[:, :, 3] * 0.26 # 26% opacity
    s2_layer = Image.fromarray(s2_arr.astype(np.uint8), mode='RGBA')
    
    # Paste on bottom-left
    bg.paste(s2_layer, (-40, height - s2_h - 40), s2_layer)
    
    # 3. Save optimized high-res JPEG
    final_rgb = bg.convert('RGB')
    bg_jpg_path = assets_dir / "calligraphy-bg.jpg"
    final_rgb.save(bg_jpg_path, format="JPEG", quality=92, optimize=True)
    
    print(f"Master background created: {bg_jpg_path} ({bg_jpg_path.stat().st_size // 1024} KB)")

if __name__ == '__main__':
    assets_dir = Path(__file__).resolve().parents[1] / 'styles' / 'ink-calligraphy' / 'assets'
    user_img1 = r'C:\Users\mailwmj\.gemini\antigravity\brain\222781ed-da9e-4964-814c-14f36b75b0e4\.user_uploaded\media_1787757924368.png'
    user_img2 = r'C:\Users\mailwmj\.gemini\antigravity\brain\222781ed-da9e-4964-814c-14f36b75b0e4\.user_uploaded\media_1787758134583.png'
    create_master_calligraphy_bg(assets_dir, user_img1, user_img2)
