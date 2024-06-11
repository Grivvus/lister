def validate_status(status: str) -> bool:
    allowed_names = ["in progress", "not started", "finished"]
    if status not in allowed_names:
        return False
    return True


def validate_rate(rate: int):
    if rate < 0 or rate > 10:
        return False
    return True
