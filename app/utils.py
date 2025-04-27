import pandas as pd

from sqlalchemy.orm import Session
from app.models import Movie

def load_movies_from_csv(db: Session, csv_path: str = None) -> None:
    """
    Load movie data from CSV file into the database.

    Args:
        db: Database session
        csv_path: Path to CSV file (defaults to assets/movielist.csv)
    """
    if csv_path is None:
        csv_path = "assets/movielist.csv"

    df = pd.read_csv(csv_path, sep = ";")

    for _, row in df.iterrows():
        movie = Movie(
            title=row["title"],
            year=row["year"],
            studios=row["studios"],
            producers=row["producers"],
            winner=True if row["winner"] == "yes" else False,
        )
        db.add(movie)

    db.commit()
