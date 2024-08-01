from typing import Any

import requests

from settings import settings

BACKEND_STRING = settings.BACKEND_STRING


async def get_all_books() -> list[dict] | None:
    response = requests.get(BACKEND_STRING + "/books/get_all_books")
    if response.status_code != 200:
        return None
    return response.json()


class Requests:
    def __init__(self, instance_name: str):
        self.instance_name = instance_name
        self.connection_string = BACKEND_STRING + "/" + instance_name + "s"

    def get_all_instance(self) -> list[dict] | None:
        """
        send request to get all items of 'instance' from db
        return list of this objects as list[dict] or
        return None if no items in db
        """
        response = requests.get(
            self.connection_string + f"/get_all_{self.instance_name}s"
        )
        if response.status_code != 200:
            return None
        return response.json()

    def get_instance_in_rate_order(self) -> list[dict] | None:
        """
        send request to get all items of 'instance' from db
        in decreasing order of rate
        return list of this objects as list[dict] or
        return None if no objects in db
        """
        response = requests.get(
            self.connection_string
            + f"/get_{self.instance_name}s_in_rate_order"
        )
        if response.status_code != 200:
            return None
        return response.json()

    def pop_instance(self) -> dict | None:
        """
        send request to get item of 'instance'
        with highest rate and status 'not started'
        returns this item and changes it status on 'in progress'
        """
        response = requests.get(
            self.connection_string + f"/pop_{self.instance_name}"
        )
        if response.status_code != 200:
            return None
        return response.json()

    def remove_instance(self, name: str) -> bool:
        """
        send request to delete item of 'instance' by name
        returns True if request was succesfull
        otherwise returns False
        """
        response = requests.delete(
            self.connection_string +
            f"/remove_{self.instance_name}/{name}"
        )
        if response.status_code != 200:
            return False
        return True

    def add_instance(self, instance_data: dict[str, Any]) -> dict | None:
        """
        send request to add item of 'instance' to db
        if addition was succesfull returns added objest
        otherwise returns None
        """
        print(instance_data)
        response = requests.post(
            url=self.connection_string + f"/add_{self.instance_name}",
            json=instance_data
        )
        if response.status_code != 200:
            return None
        return response.json()


book_requests = Requests("book")
game_requests = Requests("game")
movie_requests = Requests("movie")
