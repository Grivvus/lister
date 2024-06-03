from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_all_books():
    """
    returns all books in order of addition to db
    """
    raise NotImplementedError("not done yet")


@router.get("/get_books_in_rate_order")
def get_books_in_rate_order():
    """
    returns all books in decreasing order of rate
    """
    raise NotImplementedError("not done yet")


@router.get("/get_top_book")
def get_top_book():  # may be i'll change method name
    """
    returns book with highest rate that not read yet
    """
    raise NotImplementedError("not done yet")


@router.post("/add_book")
def add_book():
    """
    add new book to db
    """
    raise NotImplementedError("not done yet")


@router.delete("/remove_book")
def remove_book():
    # there's no id, don't know how to inentify book to delete
    """
    removing book by ???
    """
    raise NotImplementedError("not done yet")


@router.put("/change_book")
def change_book():
    # exact same problem as with delete
    """
    changing book fields
    """
    raise NotImplementedError("not done yet")
