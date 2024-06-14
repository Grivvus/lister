import pytest

from app.logic.validation import (
    validate_status,
    validate_rate,
    validate_status_and_rate
)


def test_positive_validate_status():
    assert validate_status("in progress") is True
    assert validate_status("not started") is True
    assert validate_status("finished") is True


def test_negative_validate_status():
    assert validate_status("alkdjfd") is False
    assert validate_status("inprogress") is False
    assert validate_status("IN PROGRESS") is False


def test_validate_rate():
    assert validate_rate(-1) is False
    assert validate_rate(10) is True
    assert validate_rate(0) is True
    assert validate_rate(11) is False
    assert validate_rate(3) is True
    assert validate_rate(None) is True


def test_validate_status_and_rate():
    assert validate_status_and_rate("in progress", 2) is False
    assert validate_status_and_rate("not started", 2) is False
    assert validate_status_and_rate("finished", None) is True
    assert validate_status_and_rate("in progress", None) is True
    assert validate_status_and_rate("finished", 5) is True
