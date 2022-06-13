import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint

database_name = "plantsdb"
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:eman36@127.0.0.1:5432/todoapp'
database_path ="postgresql://{}:{}@{}/{}".format('student', 'student','localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #db = SQLAlchemy(app)
    db.app = app
    db.init_app(app)
    db.create_all()
    return db


"""Plant class"""


class Plant(db.Model):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    is_poisonous = Column(Boolean)
    primary_color = Column(String)


    def __init__(self, name, scientific_name, is_poisonous, primary_color):
        self.name = name
        self.scientific_name = scientific_name
        self.is_poisonous = is_poisonous
        self.primary_color = primary_color


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "scientific_name": self.scientific_name,
            "is_poisonous": self.is_poisonous,
            "primary_color": self.primary_color,
        }
