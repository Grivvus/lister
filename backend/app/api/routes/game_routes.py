from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_all_games():
    """
    returns all games in order of addition to db
    """
    raise NotImplementedError("not done yet")


@router.get("/get_games_in_rate_order")
def get_games_in_rate_order():
    """
    returns all games in decreasing order of rate
    """
    raise NotImplementedError("not done yet")


@router.get("/get_top_game")
def get_top_game():  # may be i'll change method name
    """
    returns game with highest rate that not read yet
    """
    raise NotImplementedError("not done yet")


@router.post("/add_game")
def add_game():
    """
    add new game to db
    """
    raise NotImplementedError("not done yet")


@router.delete("/remove_game")
def remove_game():
    """
    removing game by name
    """
    raise NotImplementedError("not done yet")


@router.put("/change_game")
def change_game():
    """
    changing game fields (game identifying by name)
    """
    raise NotImplementedError("not done yet")
