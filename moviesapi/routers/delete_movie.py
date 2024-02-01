from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie

router = APIRouter()


@router.post("/delete/movie/{movie_id}", response_model=dict)
async def delete_movie(
    movie_id: int,
    session: Session = Depends(get_session),
):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    session.delete(movie)
    session.commit()
    return {"message": "Movie deleted"}
