from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from sqlmodel import Session, select,func
from db import create_db_and_tables, get_session
from models import Book

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BOOKS_PER_PAGE = 10

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/books", response_class=HTMLResponse)
def list_books(request: Request, page: int = 1, session: Session = Depends(get_session)):
    offset = (page - 1) * BOOKS_PER_PAGE
    books = session.exec(select(Book).offset(offset).limit(BOOKS_PER_PAGE)).all()
    total = session.exec(select(func.count()).select_from(Book)).one()

    has_prev = page > 1
    has_next = page * BOOKS_PER_PAGE < total

    return templates.TemplateResponse("books.html", {
        "request": request,
        "books": books,
        "page": page,
        "has_prev": has_prev,
        "has_next": has_next
    })


@app.get("/book/{book_id}", response_class=HTMLResponse)
def book_detail(request: Request, book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        return HTMLResponse("Not Found", status_code=404)
    return templates.TemplateResponse("book_detail.html", {"request": request, "book": book})

@app.get("/books/new", response_class=HTMLResponse)
def new_book_form(request: Request):
    return templates.TemplateResponse("new_book.html", {"request": request})

@app.post("/books/new", response_class=HTMLResponse)
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    total_pages: int = Form(...),
    genre: str = Form(...),
    session: Session = Depends(get_session)
):
    book = Book(title=title, author=author, year=year, total_pages=total_pages, genre=genre)
    session.add(book)
    session.commit()
    session.refresh(book)
    return RedirectResponse(url="/books/new", status_code=HTTP_302_FOUND)
