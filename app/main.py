from contextlib import asynccontextmanager
from http import HTTPStatus

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine, SessionLocal
from app.routers.awards import router as awards_router
from app.utils import load_movies_from_csv


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event for FastAPI application
    """
    db = SessionLocal()
    try:
        load_movies_from_csv(db)
    finally:
        db.close()
    yield


SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Golden Raspberry Awards API",
    description="API REST para consulta de dados do Golden Raspberry Awards na categoria Pior Filme",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(awards_router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}
