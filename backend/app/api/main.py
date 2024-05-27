from fastapi import FastAPI


def create_app():
    return FastAPI(
        title="lister api",
        version="0.1.0",
        debug=True,
        docs_url="/api/docs"
    )
