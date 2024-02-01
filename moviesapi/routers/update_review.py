from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.movie import Movie
from ..models.review import Review

router = APIRouter()


@router.post("/update/review", response_model=Review)
async def update_movie(
    review: Review,
    session: Session = Depends(get_session),
):
    review_db = session.get(Review, review.id)
    if not review_db:
        raise HTTPException(status_code=404, detail="Review not found")
    movie_db = session.get(Movie, review.movie_id)
    if not movie_db:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in review.model_dump().items():
        setattr(review_db, key, value)
    session.add(review_db)
    session.commit()
    session.refresh(review_db)
    return review_db
