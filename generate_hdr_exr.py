import numpy as np
import imageio.v3 as iio

# ‹¤’Êİ’è
width, height = 1024, 512

def create_max_luminance_image():
    img = np.zeros((height, width, 3), dtype=np.float32)
    for x in range(width):
        luminance = 400.0 + (600.0 * x / (width - 1))  # 400 to 1000 nit
        linear_rgb = luminance / 1000.0
        img[:, x, :] = linear_rgb
    return img

def create_min_luminance_image():
    img = np.zeros((height, width, 3), dtype=np.float32)
    for x in range(width):
        log_luminance = -1.5 - (2.5 * x / (width - 1))  # -1.5 to -4.0
        luminance = 10 ** log_luminance
        linear_rgb = luminance / 1000.0
        img[:, x, :] = linear_rgb
    return img

# ‰æ‘œ¶¬
max_img = create_max_luminance_image()
min_img = create_min_luminance_image()

# o—Í
iio.imwrite("ue5_hdr_max_400_1000.exr", max_img, extension=".exr")
iio.imwrite("ue5_hdr_min_log10_-1.5_-4.0.exr", min_img, extension=".exr")