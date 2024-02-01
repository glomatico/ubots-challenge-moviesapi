from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.review import Review

router = APIRouter()


@router.get("/get/review/by_review_id/{review_id}", response_model=Review)
async def get_review_by_review_id(
    review_id: int,
    session: Session = Depends(get_session),
):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.get("/get/reviews/by_movie_id/{movie_id}", response_model=list[Review])
async def get_reviews_by_movie_id(
    movie_id: int,
    session: Session = Depends(get_session),
):
    reviews = session.query(Review).filter(Review.movie_id == movie_id).all()
    return reviews


@router.get("/get/reviews", response_model=list[Review])
async def get_reviews(
    session: Session = Depends(get_session),
):
    reviews = session.query(Review).all()
    return reviews
