from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [{'title':'title one','author':'author one','category':'maths'},{'title':'title two','author':'author two','category':'sc'},{'title':'title three','author':'author three','category':'maths'},{'title':'title four','author':'author four','category':'maths'}]
@app.get("/books")
async def first_api():
    return BOOKS

@app.get("/books/{booK_title}")
async def read(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold()==book_title.casefold():
            return book


@app.get("/books/{author_name}/")
async def read_by_authorandcategory(author_name:str, category:str):
    bool =[]
    for book in BOOKS:
        if book.get("author").casefold()==author_name.casefold() and book.get("category").casefold()==category.casefold():
            bool.append(book)
    return bool

@app.post("/books/create_book")
async def create_one(new_one = Body()):
    BOOKS.append(new_one)

@app.put("/books/update")
async def update(updated_body = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==updated_body.get("title").casefold() :
            BOOKS[i] = updated_body

@app.delete("/books/delete/{booktitle}")
async def deleted(booktitle: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == booktitle.casefold():
            BOOKS.pop(i)
            break