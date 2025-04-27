import os
import datetime

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from sqlmodel import select

from app.database import get_db
from app.models import ProducerIntervalResponse, Movie, ProducerInterval, APIResponse
from app.utils import load_movies_from_csv
router = APIRouter(tags=["Awards"], prefix="/awards")


from fastapi import status

@router.get("/intervals", response_model=ProducerIntervalResponse, status_code=status.HTTP_200_OK)
async def producer_win_intervals(db: Session = Depends(get_db)):
    """
    Get producers with min and max intervals between consecutive wins

    Args:
        db: Database session (injected)

    Returns:
        Min and max intervals for producers with 200 OK status
    """
    statement = select(Movie).where(Movie.winner == True).order_by(Movie.year)

    winning_movies = db.execute(statement).scalars().all()


    producer_wins = {}

    for movie in winning_movies:
        producers = [p.strip() for p in movie.producers.replace(" and ", ", ").split(", ")]

        for producer in producers:
            if producer not in producer_wins:
                producer_wins[producer] = []

            producer_wins[producer].append(movie.year)

    min_intervals = []
    max_intervals = []

    for producer, years in producer_wins.items():
        years.sort()
        if len(years) >= 2:
            for i in range(1, len(years)):
                interval = years[i] - years[i - 1]
                producer_interval = ProducerInterval(
                    producer=producer,
                    interval=interval,
                    previousWin=years[i - 1],
                    followingWin=years[i]
                )

                if interval == 1:
                    min_intervals.append(producer_interval)
                elif interval > 1:
                    max_intervals.append(producer_interval)
    return ProducerIntervalResponse(
        min=min_intervals,
        max=max_intervals
    )


@router.post('/movies', response_model=APIResponse, status_code=status.HTTP_201_CREATED)
async def create_movies_from_csv(db: Session = Depends(get_db), file: UploadFile = File(...)):
    """
    Load movie data from uploaded CSV file into the database.

    Args:
        db: Database session
        file: Uploaded CSV file

    Returns:
        Success message with 201 Created status
    """
    if file is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file uploaded"
        )

    temp_file_path = f"/tmp/temp_movielist{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    try:
        with open(temp_file_path, "wb") as buffer:
            buffer.write(file.file.read())
        
        load_movies_from_csv(db, temp_file_path)
        return {"message": "CSV file loaded successfully", "success": True}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Error loading CSV file: {str(e)}"
        )
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)