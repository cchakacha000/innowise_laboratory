from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import models
import schemas
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(title="Book Collection API", version="1.0.0")


def get_db():
    """
    Dependency function to get database session.
    
    Yields:
        Session: Database session object
        
    Note:
        Automatically closes the session after request completion.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=schemas.BookResponse)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Add a new book to the collection.
    
    Args:
        book: Book data (title, author, year)
        db: Database session
        
    Returns:
        BookResponse: Created book with assigned ID
        
    Raises:
        HTTPException: If validation fails
    """
    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[schemas.BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """
    Retrieve all books from the collection.
    
    Args:
        db: Database session
        
    Returns:
        List[BookResponse]: List of all books
    """
    books = db.query(models.Book).all()
    return books


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a book by its ID.
    
    Args:
        book_id: Unique identifier of the book
        db: Database session
        
    Returns:
        BookResponse: Book data
        
    Raises:
        HTTPException: 404 if book not found
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book from the collection.
    
    Args:
        book_id: Unique identifier of the book to delete
        db: Database session
        
    Returns:
        dict: Success message
        
    Raises:
        HTTPException: 404 if book not found
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update book information. Only provided fields will be updated.
    
    Args:
        book_id: Unique identifier of the book to update
        book_update: Book data with fields to update (all optional)
        db: Database session
        
    Returns:
        BookResponse: Updated book data
        
    Raises:
        HTTPException: 404 if book not found
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update only provided fields
    if book_update.title is not None:
        book.title = book_update.title
    if book_update.author is not None:
        book.author = book_update.author
    if book_update.year is not None:
        book.year = book_update.year
    
    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
    title: Optional[str] = Query(None, description="Search by title (case-insensitive partial match)"),
    author: Optional[str] = Query(None, description="Search by author (case-insensitive partial match)"),
    year: Optional[int] = Query(None, description="Search by exact year"),
    db: Session = Depends(get_db)
):
    """
    Search books by title, author, or year. All parameters are optional and can be combined.
    
    Args:
        title: Book title to search (partial match, case-insensitive)
        author: Author name to search (partial match, case-insensitive)
        year: Publication year (exact match)
        db: Database session
        
    Returns:
        List[BookResponse]: List of matching books
    """
    query = db.query(models.Book)
    
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(models.Book.year == year)
    
    books = query.all()
    return books


@app.get("/")
def root():
    """
    Root endpoint providing API information and available endpoints.
    
    Returns:
        dict: API welcome message and endpoint list
    """
    return {
        "message": "Welcome to Book Collection API",
        "docs": "/docs",
        "endpoints": {
            "POST /books/": "Add a new book",
            "GET /books/": "Get all books",
            "GET /books/{book_id}": "Get book by ID",
            "PUT /books/{book_id}": "Update book details",
            "DELETE /books/{book_id}": "Delete book by ID",
            "GET /books/search/": "Search books by title, author, or year"
        }
    }

