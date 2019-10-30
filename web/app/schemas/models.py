from app import db
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):

    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)

class Tareas(db.Model):
    username=db.Column(db.String(30),unique=True,nullable=False,primary_key=True)
    tarea_1=db.Column(db.String(50),unique=True)
    tarea_2=db.Column(db.String(50),unique=True)
    tarea_3=db.Column(db.String(50),unique=True)
    tarea_4=db.Column(db.String(50),unique=True)
    tarea_5=db.Column(db.String(50),unique=True)
    tarea_6=db.Column(db.String(50),unique=True)
    tarea_7=db.Column(db.String(50),unique=True)
    tarea_8=db.Column(db.String(50),unique=True)
    tarea_9=db.Column(db.String(50),unique=True)
    tarea_10=db.Column(db.String(50),unique=True)
