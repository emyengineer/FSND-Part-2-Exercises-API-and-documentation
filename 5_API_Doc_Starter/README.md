## Book  API Documentation
# Introduction
    This API is used to perform
    CRUD operation on the Book table data base to
    Create, Read, Update and Delete Book(s) from the database
# Getting started

- Base URL
    http://127.0.0.1:5000/
- API Key : None / Not Applicable
    
# Error
- Responce Codes
    # 200
        `{"success": True}`
    # 404
        `{"success": False, "error": 404, "message": "resource not found"}`
    # 422
        `{"success": False, "error": 422, "message": "unprocessable"}`
    # 400
        `{"success": False, "error": 400, "message": "bad request"}`
- Messages
         "resource not found"
         "unprocessable"
         "bad request"
## End Points

## Resource End point Library
- **GET "/books"**
    - General: Returns a list of book objects, success value, and total number of books 
    - sample : ``curl http://127.0.0.1:5000/books``
    ```
     "books": [
                {
                  "author": "Stephen King",
                  "id": 1,
                  "rating": 3,
                  "title": "The Outsider: A Novel"
                },
                {
                  "author": "Lisa Halliday",
                  "id": 2,
                  "rating": 2,
                  "title": "Asymmetry: A Novel"
                },
                {
                  "author": "Kristin Hannah",
                  "id": 3,
                  "rating": 4,
                  "title": "The Great Alone"
                },
                {
                  "author": "Amitava Kumar",
                  "id": 7,
                  "rating": 3,
                  "title": "Immigrant, Montana"
                },
                {
                  "author": "Madeline Miller",
                  "id": 8,
                  "rating": 5,
                  "title": "CIRCE"
                },
                {
                  "author": "Gina Apostol",
                  "id": 9,
                  "rating": 5,
                  "title": "Insurrecto: A Novel"
                },
                {
                  "author": "Tayari Jones",
                  "id": 10,
                  "rating": 3,
                  "title": "An American Marriage"
                },
                {
                  "author": "Jordan B. Peterson",
                  "id": 11,
                  "rating": 5,
                  "title": "12 Rules for Life: An Antidote to Chaos"
                }
              ],
              "success": true,
              "total_books": 11
}
```
 
# PATCH UPDATE /books/<int:book_id>
 General: updates book rating based on book id returns success message and id of modified book
 Sample:
 ``
 curl http://127.0.0.1:5000/books/10 -X PATCH -H "Content-Type: application/json" -d '{"rating": "1"}'
 ``
 **`Responce`**
    {
      "id": 10,
      "success": true
    }

-  **DELETE      /books/<int:book_id>**
-  General: Deletes book by id if it exists. Returns the deleted book, success value, total books, and book list based on the current page number to update the front end
-  `sample`: **curl -X DELETE  http://127.0.0.1:5000/books/15?page=2**
-  `Response` : 
 {
      "books": [
        {
          "author": "Kiese Laymon",
          "id": 12,
          "rating": 1,
          "title": "Heavy: An American Memoir"
        },
        {
          "author": "Eman",
          "id": 24,
          "rating": 5,
          "title": "Die Empty"
        },
        {
          "author": "Neil Gaiman",
          "id": 25,
          "rating": 5,
          "title": "NeverWhere"
        }
  ],
  "deleted": 15,
  "success": true,
  "total_books": 11
}

    `arguments:` **book_id**  integer

-  **POST  "/books"**
    General : Create new book using the submitted title, author, rating. Returns id of the created book, success and book list based on current page number to update the front end
    `sample`: 
      ``curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title": "NeverWhere", "author": "Neil Gaiman", "rating":"5"  }'``
Response 
{
          "books": [],
          "created": 25,
          "success": true,
          "total_books": 12
}

    `search_term Mode`: has value
   
    `Create Mode`: search term is None it will add new book to the D.B
   
