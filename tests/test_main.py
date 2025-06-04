# -*- coding: utf-8 -*-
# @Author: hugodms
# @Date:   2025-06-04 12:21:52
# @Last Modified by:   hugodms
# @Last Modified time: 2025-06-04 15:24:16

import subprocess
import pytest


@pytest.mark.parametrize(
    "filename,expected_output",
    [
        ("invoice_document.png", "Detected Tables : 1"),
        ("bank_document.png", "Detected Tables : 1"),
        ("empty_document.png", "Detected Tables : 0"),
        ("does_not_exist.png", "File not found:"),
        ("document.txt", "Unsupported format."),
    ],
)
def test_main_script(filename, expected_output):
    full_path = "./assets/" + filename
    result = subprocess.run(
        ["python", "main.py", filename], capture_output=True, text=True
    )
    assert expected_output in result.stdout or expected_output in result.stderr
