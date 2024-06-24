import pytest
from fastapi import HTTPException

from app.logic.validation import (
    validate_status,
    validate_rate,
    validate_status_and_rate
)


def test_positive_validate_status():
    validate_status("in progress")
    validate_status("not started")
    validate_status("finished")


def test_negative_validate_status():
    with pytest.raises(HTTPException) as e:
        validate_status("alkdjfd")
        assert e.status_code == 422
        assert e.detail == "wrong status"
    with pytest.raises(HTTPException) as e:
        validate_status("inprogress")
        assert e.status_code == 422
        assert e.detail == "wrong status"
    with pytest.raises(HTTPException) as e:
        validate_status("IN PROGRESS")
        assert e.status_code == 422
        assert e.detail == "wrong status"


def test_validate_rate():
    validate_rate(10)
    validate_rate(0)
    validate_rate(3)
    validate_rate(None)

    with pytest.raises(HTTPException) as e:
        validate_rate(-1)
        assert e.status_code == 422
        assert e.detail == f"wrond rate: {-1} rate is >= 0 and <= 10"

    with pytest.raises(HTTPException) as e:
        validate_rate(11)
        assert e.status_code == 422


def test_validate_status_and_rate():
    validate_status_and_rate("finished", None)
    validate_status_and_rate("in progress", None)
    validate_status_and_rate("finished", 5)

    with pytest.raises(HTTPException) as e:
        validate_status_and_rate("not started", 2)
        assert e.status_code == 422

    with pytest.raises(HTTPException) as e:
        validate_status_and_rate("in progress", 2)
        assert e.status_code == 422
