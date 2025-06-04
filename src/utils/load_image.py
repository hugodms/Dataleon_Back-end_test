# -*- coding: utf-8 -*-
# @Author: hugodms
# @Date:   2025-06-04 14:55:33
# @Last Modified by:   hugodms
# @Last Modified time: 2025-06-04 15:13:18

from PIL import Image, UnidentifiedImageError

def load_image(image_path):
    if not image_path.lower().endswith((".png", ".jpg", ".jpeg")):
        raise ValueError("Unsupported format. Please use a .png, .jpg, or .jpeg image.")

    try:
        return Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {image_path}")
    except UnidentifiedImageError:
        raise UnidentifiedImageError("The specified file is not a valid image.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while loading image: {str(e)}")