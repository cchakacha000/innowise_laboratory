from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    """
    SQLAlchemy model representing a book in the database.
    
    Attributes:
        id: Primary key, auto-incremented integer
        title: Book title (required)
        author: Book author (required)
        year: Publication year (optional)
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

