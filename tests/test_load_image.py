# -*- coding: utf-8 -*-
# @Author: hugodms
# @Date:   2025-06-04 15:24:00
# @Last Modified by:   hugodms
# @Last Modified time: 2025-06-04 15:26:49

import pytest
from PIL import UnidentifiedImageError
from src.utils.load_image import load_image


def test_load_valid_image():
    image = load_image("assets/invoice_document.png")
    assert image.mode == "RGB"


def test_invalid_extension():
    with pytest.raises(ValueError, match="Unsupported format"):
        load_image("assets/document.txt")


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_image("assets/does_not_exist.png")


def test_invalid_image_content(tmp_path):
    invalid_file = tmp_path / "fake.jpg"
    invalid_file.write_text("not really an image")
    with pytest.raises(UnidentifiedImageError):
        load_image(str(invalid_file))
