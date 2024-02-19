import json

import requests

BASE_URL = "http://127.0.0.1:8000"

def check_for_permition(user_id: int, obj_id: int, obj_type: str):
    if obj_type not in ["book", "game", "movie"]:
        raise ValueError("Object type must be 'book' or 'game' or 'movie'")
    data = {"user_id": user_id, "obj_id": obj_id}
    r = requests.post(
        f"{BASE_URL}/check_for_permition/{obj_type}", data=json.dumps(data)
    )
    if r.status_code >= 400:
        raise ConnectionRefusedError()
    if r.content.decode() == "true":
        return True
    return False
