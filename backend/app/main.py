from fastapi import FastAPI

from app.api.main import api_router
from app.core.db import start_async_mongodb


app = FastAPI(
        debug=True, title="lister",
        docs_url="/", version="0.1.0",
    )
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup_event() -> None:
    await start_async_mongodb()


if __name__ == "__main__":
    msg = "don't forget to "\
    + "export PYTHONPATH=/home/grivvus/Py_Projects/lister/backend"
    print(msg)
