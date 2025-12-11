from pydantic import BaseModel, Field
from typing import Optional


class BookBase(BaseModel):
    """Base schema with common book fields."""
    title: str = Field(..., description="Book title")
    author: str = Field(..., description="Book author")
    year: Optional[int] = Field(None, description="Publication year")


class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass


class BookUpdate(BaseModel):
    """Schema for updating book information. All fields are optional."""
    title: Optional[str] = Field(None, description="Book title")
    author: Optional[str] = Field(None, description="Book author")
    year: Optional[int] = Field(None, description="Publication year")


class BookResponse(BookBase):
    """Schema for book response, includes book ID."""
    id: int

    class Config:
        from_attributes = True

