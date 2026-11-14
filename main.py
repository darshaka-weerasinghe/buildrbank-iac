"""
The entrypoint Vercel looks for.

Vercel finds a FastAPI app by looking for a variable called `app` in a file
called main.py (or app.py, index.py, server.py). Ours is called `api` and
lives in app/api.py, which is what Docker and uvicorn use. This file is the
one-line bridge between the two names. Nothing else changes.
"""
from app.api import api as app  # noqa: F401
