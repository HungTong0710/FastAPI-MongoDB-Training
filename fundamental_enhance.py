# We will write this code LIVE together at the workshop!
# Keep this file empty for now, see you there!
from fastapi import FastAPI, Path, Query, status, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

#--------------------
#ENHANCE VERSION:
# Pydantic model & Field Validation --> POST, PUT
# Path & Query Validation --> pynamic params
# Status code & HTTP exception
#--------------------

#--------------------
#OVERALL
# CRUD methods
# Path & Query params
# Pydantic - Field, Path, Query Validations
# Status Code & HTTP exception
#--------------------

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

#Pydantic model
class BookRequest(BaseModel):
   id: Optional[int] = Field(default= None, description= "ID not needed to create")
   title: str = Field(min_length= 3) 
   author: str = Field(min_length= 1)
   category: str = Field(min_length = 2, max_length= 100)
   rating: int = Field(gt = 0, lt = 6)

   # Swagger configuration
   model_config = {
      "json_schema_extra": {
         "example": {
            "title": "new book",
            "author": "Nguyen Van A",
            "category": "history",
            "rating": 5
         }
      }
   }

# GET request
#decorator
@app.get("/books", status_code= status.HTTP_200_OK)
async def read_books():
 return BOOKS

# Order matters
@app.get("/books/my-book", status_code= status.HTTP_200_OK)
async def my_favorite_book():
   return {"My book": "My favorite book"}

# Path parameters
@app.get("/books/{book_title}", status_code= status.HTTP_200_OK)
async def read_book_by_path(book_title: str = Path(min_length= 3)):
   for book in BOOKS:
      if book.title.casefold() == book_title.casefold():
         return book
   raise HTTPException(status_code= 404, detail= "item not found")
 
#Query parameters
@app.get("/books/", status_code= status.HTTP_200_OK)
async def read_book_by_query(book_title: str = Query(min_length= 3)):
   for book in BOOKS:
      if book.title.casefold() == book_title.casefold():
         return book
   raise HTTPException(status_code= 404, detail= "item not found")

def find_book_id(book: Book):
   book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
   return book

#POST, PUT, DELETE method
@app.post("/create-book", status_code= status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
   new_book = Book(**book_request.model_dump())
   new_book = find_book_id(new_book)
   BOOKS.append(new_book)

#PUT method
@app.put("/books/update-book", status_code= status.HTTP_204_NO_CONTENT)
async def update_book(book_updated: BookRequest):
   book_changed = False
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book_updated.get("id"):
         BOOKS[i] = Book(**book_updated.model_dump())
         book_changed = True
   if not book_changed:
      raise HTTPException(status_code= 404, detail= "item not found")

#DELETE method
@app.delete("/books/delete-book/{book_id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt = 0)):
   book_changed = False
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book_id:
         BOOKS.pop(i)
         book_changed = True
         break
   if not book_changed:
      raise HTTPException(status_code= 404, detail= "item not found")



      