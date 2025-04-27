import io

from fastapi import status
from sqlmodel import select


def test_upload_movies_csv_success(client, session):
    """Test successful CSV file upload"""
    csv_content = "year;title;studios;producers;winner\n" \
                  "2010;Test Movie Upload;Studio Test;Upload Producer;yes\n" \
                  "2011;Another Test;Studio ABC;Another Producer;no\n"

    csv_file = io.BytesIO(csv_content.encode())

    response = client.post(
        "/awards/movies",
        files={"file": ("test.csv", csv_file, "text/csv")}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "CSV file loaded successfully", "success": True}

    from app.models import Movie
    movies = session.execute(select(Movie).order_by(Movie.year)).scalars().all()

    assert len(movies) == 2

    movie_titles = [movie.title for movie in movies]
    assert "Test Movie Upload" in movie_titles
    assert "Another Test" in movie_titles

    for movie in movies:
        if movie.title == "Test Movie Upload":
            assert movie.winner is True
        if movie.title == "Another Test":
            assert movie.winner is False


def test_upload_invalid_csv(client):
    """Test upload with invalid CSV format"""
    csv_content = "year;title;studios\n" \
                  "2010;Invalid Movie;Studio Test\n"

    csv_file = io.BytesIO(csv_content.encode())

    response = client.post(
        "/awards/movies",
        files={"file": ("invalid.csv", csv_file, "text/csv")}
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "Error loading CSV file" in response.json()["detail"]


def test_upload_no_file(client):
    """Test upload with no file provided"""
    response = client.post("/awards/movies")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

