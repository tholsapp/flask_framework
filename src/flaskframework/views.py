#!env/bin/python
from flask import render_template

from src.flaskframework import app


@app.route('/')
def index():
  #return '<h1>Hello World!</h1>'
  return render_template('index.html')

