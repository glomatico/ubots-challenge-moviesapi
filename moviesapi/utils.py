from datetime import datetime, time

from fastapi.exceptions import HTTPException

from .models.movie import Movie


def convert_date_and_time(movie: Movie):
    try:
        movie.release_date = datetime.fromisoformat(movie.release_date)
        movie.duration = time.fromisoformat(movie.duration)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date or time format",
        )
