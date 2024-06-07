from fastapi import FastAPI

from app.api.main import api_router


def fastapi_factory():
    api_instance = FastAPI(
        debug=True, title="lister",
        docs_url="/", version="0.1.0",
    )
    api_instance.include_router(api_router, prefix="/api")

    return api_instance


if __name__ == "__main__":
    msg = "don't forget to "\
    + "export PYTHONPATH=/home/grivvus/Py_Projects/lister/backend"
    print(msg)
