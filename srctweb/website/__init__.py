from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


srctweb = Flask(__name__)
srctweb.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
srctweb.secret_key = "this_is_a_terrible_secret_key"
db = SQLAlchemy(srctweb)

from website import views
from website import models
from website import admin
