def validate_status(status: str) -> bool:
    allowed_names = ["in progress", "not started", "finished"]
    if status not in allowed_names:
        return False
    return True


def validate_rate(rate: int):
    """
    rate is a number between 0 and 10
    """
    if rate < 0 or rate > 10:
        return False
    return True


def validate_status_and_rate(status: str, rate: int | None):
    """
    rate should be 'None' if status != 'finished'
    """
    if status != "finished" and rate is not None:
        return False
    return True
