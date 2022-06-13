from flask import Flask, jsonify
from models import setup_db, Plant
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    #app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    #CORS(app, resources={r'*/api/*': {'origins': '*'}})
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return jsonify({'message': 'Hello World'})

    @app.route('/smily')
    def smily():
        return ':)'
    
    #@cross_origin
    @app.route('/cors')
    def test_cors():
        return "CORS please connect me to the origin"

    return app