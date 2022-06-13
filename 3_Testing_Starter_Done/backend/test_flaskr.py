import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "eman36", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_book = {"title": "Anansi Boys", "author": "Neil Gaiman", "rating": 5}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    # #1 -- Get All
    # def test_Get_All_Books(self):
    #     '''Test Getting All Books Success: True Ok '''
    #     res = self.client().get('/books')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))

    # #2 -- Get Page does not Exist
    # def test_404_requesting_valid_page(self):
    #     '''page number invalid'''
    #     res = self.client().get('/books?page=1000', json={'rating': 1})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    #3 -- Partially update Rating using  - PATCH
    # def test_update_partially_patch(self):
    #     '''Test update value/part of the book '''
    #     res = self.client().patch('/books/{}'.format(11), json={"rating": 4})
    #     data = json.loads(res.data)
    #     book = Book.query.filter(Book.id == 11).one_or_none()
    #     print(book.format())
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(book.format()["rating"] , 4)
        
    #4 -- Failed Update
    # def test_update_err(self):
    #     '''Test update with 400 error for abort'''
    #     res = self.client().patch('/books/{}'.format(11)) # removed , json={"rating": 4}
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "bad request")
                
    #def 

    
    # def test_Get_All_Books_Error(self):
    #     '''Test Getting All Books Success: False'''
    #     res = self.client().get('/books/1')
    #     self.assertEqual(res.status_code, 200)


    # def test_delete_book(self):
    #     '''Test Delete Book'''
    #     res = self.client().delete('/books/{}'.format(2))
    #     data = json.loads(res.data)
    #     #print(data)
    #     book = Book.query.filter(Book.id == 2).one_or_none()
    #     self.assertEqual(res.status_code, 200)
    #     #self.assertEqual(data["success"], True)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(data['deleted'], 2)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))
    #     self.assertEqual(book, None)
        

   # Book doesnot exist 
    def test_Delete_book_err(self):
        '''Test Delete Book with Error'''
        res = self.client().delete('/books/{}'.format(1000))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    #Add new book
    def test_Add_book(self):
        '''Test Add new book'''
        res = self.client().post('/books', json={"title": "Anansi Boys", "author": "Neil Gaiman", "rating": 5})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"]) 
        self.assertTrue(len(data["books"]))

    def test_405_if_book_creation_not_allowed(self):
        res = self.client().post("/books/45", json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")



    


   

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc.
#        Since there are four routes currently, you should have at least eight tests.
# Optional: Update the book information in setUp to make the test database your own!


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
