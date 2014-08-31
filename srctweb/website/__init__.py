from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


srctweb = Flask(__name__)
srctweb.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy( srctweb )


from website import views
from website import models
