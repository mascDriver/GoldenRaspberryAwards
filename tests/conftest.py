import os
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.database import get_db
from app.models import Movie


@pytest.fixture(name="test_db_engine")
def test_db_engine_fixture():
    """Create a test database engine"""
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="session")
def session_fixture(test_db_engine):
    """Create a test database session"""
    with Session(test_db_engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session):
    """Create a FastAPI test client with the test database"""
    def get_test_db():
        try:
            yield session
        finally:
            pass

    app.dependency_overrides[get_db] = get_test_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="sample_movies")
def sample_movies_fixture(session):
    """Create sample movies for testing"""
    movies = [
        Movie(
            year=1980,
            title="Test Movie 1",
            studios="Studio A",
            producers="John Producer",
            winner=True
        ),
        Movie(
            year=1981,
            title="Test Movie 2",
            studios="Studio B",
            producers="John Producer",
            winner=True
        ),
        Movie(
            year=1985,
            title="Test Movie 3",
            studios="Studio A",
            producers="Jane Producer",
            winner=True
        ),
        Movie(
            year=1990,
            title="Test Movie 4",
            studios="Studio C",
            producers="Jane Producer",
            winner=True
        ),
        Movie(
            year=2000,
            title="Test Movie 5",
            studios="Studio D",
            producers="New Producer",
            winner=False
        )
    ]
    
    for movie in movies:
        session.add(movie)
    session.commit()
    
    for movie in movies:
        session.refresh(movie)
        
    return movies
