# We will write this code LIVE together at the workshop!
# Keep this file empty for now, see you there!
from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    category: str
    rating: str
    def __init__(self, id, title, author, category, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.rating = rating

# mock data
BOOKS = [
    Book(1,"Learning FastAPI from scratch", "Hung Tong", "science", 5),
    Book(2,"F1", "Hung Tong", "science", 3),
    Book(3,"F2", "Hung Tong", "math", 5),
    Book(4,"F3", "Hung Tong", "math", 4),
    Book(5,"F4", "Hung Tong", "history", 2)
]

class BookRequest(BaseModel):
   id: int
   title: str 
   author: str
   category: str
   rating: int
   # Swagger configuration
   model_config = {
      "json_schema_extra": {
         "example": {
            "id": 6,
            "title": "new book",
            "author": "Nguyen Van A",
            "category": "history",
            "rating": 5
         }
      }
   }

# GET request
#decorator
@app.get("/books")
async def read_books():
 return BOOKS

# Order matters
@app.get("/books/my-book")
async def my_favorite_book():
   return {"My book": "My favorite book"}

# Path parameters
@app.get("/books/{book_title}")
async def read_book_by_path(book_title: str):
   for book in BOOKS:
      if book.title.casefold() == book_title.casefold():
         return book
      
#Query parameters
@app.get("/books/")
async def read_book_by_query(book_title: str):
   for book in BOOKS:
      if book.title.casefold() == book_title.casefold():
         return book

#POST, PUT, DELETE method
@app.post("/create-book")
async def create_book(Book_request: BookRequest):
   new_book = Book(**Book_request.model_dump())
   BOOKS.append(new_book)

#PUT method
@app.put("/books/update-book")
async def update_book(book_updated = Body()):
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book_updated.get("id"):
         BOOKS[i] = book_updated

#DELETE method
@app.delete("/books/delete-book/{book_id}")
async def delete_book(book_id: int):
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book_id:
         BOOKS.pop(i)
         break



      