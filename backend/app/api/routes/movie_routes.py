from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_all_movies():
    """
    returns all movies in order of addition to db
    """
    raise NotImplementedError("not done yet")


@router.get("/get_movies_in_rate_order")
def get_movies_in_rate_order():
    """
    returns all movies in decreasing order of rate
    """
    raise NotImplementedError("not done yet")


@router.get("/get_top_movie")
def get_top_movie():  # may be i'll change method name
    """
    returns movie with highest rate that not read yet
    """
    raise NotImplementedError("not done yet")


@router.post("/add_movie")
def add_movie():
    """
    add new movie to db
    """
    raise NotImplementedError("not done yet")


@router.delete("/remove_movie")
def remove_movie():
    """
    removing movie by name
    """
    raise NotImplementedError("not done yet")


@router.put("/change_movie")
def change_movie():
    """
    changing movie fields (identifying by name)
    """
    raise NotImplementedError("not done yet")
