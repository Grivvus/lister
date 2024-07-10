import requests

from settings import settings

BACKEND_STRING = settings.BACKEND_STRING


async def get_all_books() -> list[dict] | None:
    response = requests.get(BACKEND_STRING + '/books/get_all_books')
    if response.status_code != 200:
        return None
    return response.json()
