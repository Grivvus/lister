from fastapi import HTTPException


def validate_status(status: str) -> bool:
    allowed_names = ["in progress", "not started", "finished"]
    if status not in allowed_names:
        raise HTTPException(status_code=422, detail="wrong status")


def validate_rate(rate: int | None):
    """
    rate is a number between 0 and 10
    """
    if rate is not None and (rate < 0 or rate > 10):
        raise HTTPException(status_code=422, detail="wrong rate")


def validate_status_and_rate(status: str, rate: int | None):
    """
    rate should be 'None' if status != 'finished'
    """
    if status != "finished" and rate is not None:
        raise HTTPException(
            status_code=422,
            detail="you cannot rate book if you not finished it yet"
        )


def validate_status_and_review(status: str, review: str):
    """
    review should be 'None' if status != 'finished'
    """
    if status != "finished" and review is not None:
        raise HTTPException(
            status_code=422,
            detail="you cannot have a reiview on unfinished stuff"
        )
