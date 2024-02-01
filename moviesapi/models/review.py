from typing import Optional

from sqlmodel import Field, SQLModel


class Review(SQLModel, table=True, arbitrary_types_allowed=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stars: int
    comment: str
    movie_id: int = Field(default=None, foreign_key="movie.id")
