# starts backend service locally with debug info
# poetry shell
# uvicorn  --factory app.main:fastapi_factory --reload --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
