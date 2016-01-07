#!env/bin/python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)

def init_webapp():
  """ Initialize the web app """

  """ Iniitialize Flask Configuration """
  app.config.from_object('config')

  return app


from main import views
