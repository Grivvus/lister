from typing import Any
import datetime


def response_to_text(response):
    """not written yet"""
    return response.__str__()


def prepair_insert_data_to_request(
    data: dict[str, Any]
) -> dict[str, Any]:
    data["add_time"] = datetime.datetime.now().isoformat()
    data["change_time"] = None
    data["rate"] = data.get("rate", None)
    data["review"] = data.get("review", None)

    return data
