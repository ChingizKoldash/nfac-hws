from typing import Optional
from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int
    total_pages: int
    genre: str
