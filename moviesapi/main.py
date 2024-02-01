from fastapi import FastAPI

from .database import create_database
from .routers import (
    create_movie,
    create_review,
    delete_movie,
    delete_review,
    get_movie,
    get_review,
    root,
    update_movie,
    update_review,
)

app = FastAPI()
app.include_router(create_movie.router)
app.include_router(create_review.router)
app.include_router(delete_movie.router)
app.include_router(delete_review.router)
app.include_router(get_movie.router)
app.include_router(get_review.router)
app.include_router(root.router)
app.include_router(update_movie.router)
app.include_router(update_review.router)


@app.on_event("startup")
async def startup():
    create_database()
