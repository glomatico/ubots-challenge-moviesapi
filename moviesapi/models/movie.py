from datetime import datetime, time
from typing import Optional

from sqlmodel import Field, SQLModel


class Movie(SQLModel, table=True, arbitrary_types_allowed=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    synopsis: str
    language: str
    rating: str
    release_date: datetime
    duration: time
