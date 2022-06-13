import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        #Access-Control-Allow-Origin
        #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        #'Access-Control-Allow-Credentials'
     
        return response

    # @GET ALL: Write a route that retrivies all books, paginated.
    #         You can use the constant above to paginate by eight books.
    #         If you decide to change the number of books per page,
    #         update the frontend to handle additional books in the styling and pagination
    #         Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, the webpage will display books including title, author, and rating shown as stars

    @app.route('/books', methods=['GET'])
    def get_books():
        page = request.args.get('page', 1, type=int)
        start = (page -1) * BOOKS_PER_SHELF
        end = start + BOOKS_PER_SHELF
        books = Book.query.all()
        formatted_books = [book.format() for book in books] 
        return jsonify({
            'success': True,
            'books': formatted_books[start:end],
            'total_books': len(formatted_books)
        })

    # @TODO: Write a route that will update a single book's rating.
    #         It should only be able to update the rating, not the entire representation
    #         and should follow API design principles regarding method and route.
    #         Response body keys: 'success'
    # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh
    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_rating(book_id):
        body = request.get_json()
        new_rating = body.get("rating", None)
       
        bookToBeUpdated = Book.query.filter(Book.id == book_id).one_or_none()
        bookToBeUpdated.rating = new_rating
        bookToBeUpdated.update()
        if bookToBeUpdated is None:
            abort(404)
        #books = Book.query.all()
        #formatted_books = [book.format() for book in books] 
        return jsonify({
            'success': True,
            'id': bookToBeUpdated.id
         })

    # @DELETE: Write a route that will delete a single book.
    #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
    #        Response body keys: 'success', 'books' and 'total_books'
    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        page = request.args.get('page', 1, type=int)
        start = (page -1) * BOOKS_PER_SHELF
        end = start + BOOKS_PER_SHELF
        bookToBeDeleted = Book.query.filter(Book.id == book_id).one_or_none()
        print("Book to be deleted {}".format(bookToBeDeleted))
        bookToBeDeleted.delete()
        books = Book.query.all()
        formatted_books = [book.format() for book in books] 
        return jsonify({
            'success': True,
            'books': formatted_books[start:end],
            'total_books': len(formatted_books),
            'deleted': bookToBeDeleted.id
        })

    # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.

    # @TODO: Write a route that create a new book.
    #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
    # TEST: When completed, you will be able to add a new book using the form. Try doing so from the last page of books.
    #       Your new book should show up immediately after you submit it at the end of the page.
    @app.route('/books', methods=['POST'])
    def create_book():
        try:
            print('Create Book Started')
            body = request.get_json()
            add_title = body.get("title", None)
            add_author = body.get("author", None)
            add_rating = body.get("rating", None)
            addBook = Book(title=add_title , author=add_author, rating=add_rating)
            addBook.insert()
            page = request.args.get('page', 1, type=int)
            start = (page -1) * BOOKS_PER_SHELF
            end = start + BOOKS_PER_SHELF
            books = Book.query.order_by(Book.id).all()
            formatted_books = [book.format() for book in books] 

            return jsonify({
                'success': True,
                'books': formatted_books[start:end],
                'total_books': len(formatted_books),
                'created': addBook.id
            })
        except:
            abort(422)

    return app
