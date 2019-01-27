#!env/bin/python

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)

def init_webapp():
  """ Initialize the web app """

  """ Iniitialize Flask Configuration """
  app.config.from_object('config')

  Bootstrap(app)
  return app


from src.flaskframework import views
