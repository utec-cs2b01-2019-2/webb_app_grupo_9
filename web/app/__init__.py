from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



dbdir="sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]=dbdir


app.secret_key='..'

from routes import *