from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id1: int
    title: str
    description: str
    rating: int

    def __init__(self, id1, title, description, rating):
        self.id1 = id1
        self.title = title
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id1: Optional[int] = None
    title: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)


def find_book(book: Book):
    if len(books) > 0:
        book.id1 = books[-1].id1 + 1
    else:
        book.id1 = 1
    return book


books = [Book(1, 'master python', 'a good book', 3),
        Book(2, 'master pycharm', 'a nice book', 4),
        Book(3, 'master fastapi', 'a good book', 2)

        ]


@app.get("/book")
async def read():
    return books


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_one = Book(**book_request.model_dump())
    books.append(find_book(new_one))

# @app.post("/book/booktocreate")
# async def create(book_request=Body()):
#     book.append(book_request)
