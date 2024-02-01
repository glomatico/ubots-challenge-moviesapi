from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie
from ..models.review import Review

router = APIRouter()


@router.post("/create/review", response_model=Review)
async def create_review(
    review: Review,
    session: Session = Depends(get_session),
):
    if review.id is not None:
        raise HTTPException(status_code=400, detail="Id should not be provided")
    movie_db = session.get(Movie, review.movie_id)
    if not movie_db:
        raise HTTPException(status_code=404, detail="Movie not found")
    session.add(review)
    session.commit()
    session.refresh(review)
    return review
