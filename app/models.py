from typing import Optional

from sqlmodel import Field, SQLModel


class Movie(SQLModel, table=True):
    """Movie entity representing a movie in the Golden Raspberry Awards"""
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int
    title: str
    studios: str
    producers: str
    winner: bool = Field(default=False)


class ProducerInterval(SQLModel):
    """Schema for producer interval data"""
    producer: str
    interval: int
    previousWin: int
    followingWin: int


class ProducerIntervalResponse(SQLModel):
    """Schema for producer interval response with min and max lists"""
    min: list[ProducerInterval]
    max: list[ProducerInterval]


class APIResponse(SQLModel):
    """Standard API response model for operations"""
    message: str
    success: bool


class APIResponse(SQLModel):
    """Standard API response model for operations"""
    message: str
    success: bool
