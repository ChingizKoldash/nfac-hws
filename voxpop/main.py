from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Integer, String, DateTime, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Настройка БД
DATABASE_URL = "sqlite:///voxpop.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Модель комментария
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Создание таблицы при старте
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

COMMENTS_PER_PAGE = 5

@app.get("/")
def index(request: Request, page: int = 1, filter: str = "all"):
    with SessionLocal() as db:
        query = db.query(Comment)
        if filter in ["positive", "negative"]:
            query = query.filter(Comment.category == filter)

        total_count = query.count()
        total_pages = (total_count - 1) // COMMENTS_PER_PAGE + 1 if total_count else 1

        comments = (
            query.order_by(Comment.id.desc())
            .offset((page - 1) * COMMENTS_PER_PAGE)
            .limit(COMMENTS_PER_PAGE)
            .all()
        )

    return templates.TemplateResponse("index.html", {
        "request": request,
        "comments": comments,
        "page": page,
        "total_pages": total_pages,
        "filter": filter,
    })

@app.post("/submit")
def submit_comment(text: str = Form(...), category: str = Form(...)):
    if category not in ["positive", "negative"] or not text.strip():
        return RedirectResponse("/", status_code=303)

    with SessionLocal() as db:
        comment = Comment(text=text.strip(), category=category)
        db.add(comment)
        db.commit()

    return RedirectResponse("/", status_code=303)
