from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie
from ..utils import convert_date_and_time

router = APIRouter()


@router.post("/create/movie", response_model=Movie)
async def create_movie(
    movie: Movie,
    session: Session = Depends(get_session),
):
    convert_date_and_time(movie)
    if movie.id is not None:
        raise HTTPException(status_code=400, detail="Id should not be provided")
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie
