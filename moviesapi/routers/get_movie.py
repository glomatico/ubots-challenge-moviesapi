from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie

router = APIRouter()


@router.get("/get/movie/{movie_id}", response_model=Movie)
async def get_movie_by_movie_id(
    movie_id: int,
    session: Session = Depends(get_session),
):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.get("/get/movies", response_model=list[Movie])
async def get_movies(
    session: Session = Depends(get_session),
):
    movies = session.query(Movie).all()
    return movies
