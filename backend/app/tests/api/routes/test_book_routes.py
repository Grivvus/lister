import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_get_all_books():
    response = client.get(
        "/api/books/get_all_books",
        headers={"accept": "application/json"}
    )
    assert response.status_code == 200


def test_get_books_in_rate_order():
    ...


def test_pop_book():
    """
    написать тесты, когда сделаю метод идемпотентным
    """


def test_add_book():
    valid_book_1 = {"book_data": {
        "name": "Сказка о золотой рыбке",
        "status": "not started",
        "rate": None,
        "review": None,
        "add_time": "2024-06-24T07:54:13.634000Z",
        "change_time": None,
        "author": "A. S. Pushkin",
        "book_genre": "fairy tail"
    }}
    valid_book_2 = {
        "name": "Ревизор",
        "status": "finished",
        "rate": 5,
        "review": "забавная шляпа",
        "add_time": "2024-06-24T07:54:13.634000Z",
        "change_time": "2024-06-24T07:54:13.634000Z",
        "author": "Н. В. Гоголь",
        "book_genre": "play"
    }

    response = client.post("api/books/add_book", json=valid_book_1)
    assert response.status_code == 200

    response = client.post("api/books/add_book",  json=valid_book_2)
    assert response.status_code == 200
