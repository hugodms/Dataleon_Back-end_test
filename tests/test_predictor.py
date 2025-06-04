# -*- coding: utf-8 -*-
# @Author: hugodms
# @Date:   2025-06-04 12:13:19
# @Last Modified by:   hugodms
# @Last Modified time: 2025-06-04 15:24:30

import pytest

from src.model.predictor import TableDetector

INVOICE_IMAGE = "assets/invoice_document.png"
BANK_IMAGE = "assets/bank_document.png"
FAKE_IMAGE = "assets/does_not_exist.png"
EMPTY_IMAGE = "assets/empty_document.png"

detector = TableDetector()


def test_model_loads():
    assert detector.model is not None
    assert detector.processor is not None


def test_predict_invoice_image():
    result = detector.predict(INVOICE_IMAGE)
    assert "tables" in result
    assert isinstance(result["tables"], list)
    assert result["num_tables"] >= 1


def test_predict_invoice_image():
    result = detector.predict(BANK_IMAGE)
    assert "tables" in result
    assert isinstance(result["tables"], list)
    assert result["num_tables"] >= 1


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        detector.predict(FAKE_IMAGE)


def test_image_without_table():
    result = detector.predict(EMPTY_IMAGE)
    assert result["num_tables"] == 0
    assert result["tables"] == []
