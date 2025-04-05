from sqlmodel import SQLModel, create_engine, Session, select
from models import Book

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    # insert_sample_data()


def get_session():
    with Session(engine) as session:
        yield session


# def insert_sample_data():
#     with Session(engine) as session:
#         books_in_db = session.exec(select(Book)).first()
#         if books_in_db:
#             return  # Уже есть данные, ничего не делаем

#         for i in range(1, 51):
#             book = Book(
#                 title=f"Тестовая книга {i}",
#                 author=f"Автор {i}",
#                 year=2000 + i,
#                 total_pages=100 + i,
#                 genre="Фантастика" if i % 2 == 0 else "Роман"
#             )
#             session.add(book)
#         session.commit()
