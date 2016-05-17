#ourapp/__init__.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,instance_relative_config=True)

app.config.from_object('config')

app.config.from_pyfile('config.py')

db.SQLAlchemy(app)


#ourapp/model.py

from . import db

class Engine(db.Model):

#columns

id=db.Column(db.db.Integer,primary_key=True, autoincrement=True)
title=db.Column(db.String(128))

thrust=db.Column(db.Integer,default=0)


