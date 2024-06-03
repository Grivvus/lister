# starts backend service locally with debug info
uvicorn --factory app.main:fastapi_factory --reload --host 0.0.0.0 --port 8000
