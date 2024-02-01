from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from ..dependencies import get_session
from ..models.review import Review

router = APIRouter()


@router.post("/delete/review/delete_by_review_id/{review_id}", response_model=dict)
async def delete_review(
    review_id: int,
    session: Session = Depends(get_session),
):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    session.delete(review)
    session.commit()
    return {"message": "Review deleted"}


@router.post("/delete/reviews/delete_by_movie_id/{movie_id}", response_model=dict)
async def delete_reviews(
    movie_id: int,
    session: Session = Depends(get_session),
):
    reviews = session.query(Review).filter(Review.movie_id == movie_id).all()
    if not reviews:
        raise HTTPException(status_code=404, detail="Reviews not found")
    for review in reviews:
        session.delete(review)
    session.commit()
    return {"message": "Reviews deleted"}
