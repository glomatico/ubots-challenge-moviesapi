from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie
from ..utils import convert_date_and_time

router = APIRouter()


@router.post("/update/movie", response_model=Movie)
async def update_movie(
    movie: Movie,
    session: Session = Depends(get_session),
):
    convert_date_and_time(movie)
    movie_db = session.get(Movie, movie.id)
    if not movie_db:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.model_dump().items():
        setattr(movie_db, key, value)
    session.add(movie_db)
    session.commit()
    session.refresh(movie_db)
    return movie_db
