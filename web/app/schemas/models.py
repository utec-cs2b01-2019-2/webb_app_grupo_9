from app import db
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() 

class Users(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)

class Tareas(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)