import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)


with open('db_login.txt') as f:
    db_login = f.readline().replace('\n', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_login

db = SQLAlchemy(app)

from python_src import routes

