#!./venv/bin/python

from configobj import ConfigObj

from flask_script import Manager

from src.config import config
from src.flaskframework import app, init_webapp

manager = Manager(app)


""" Start Server """
@manager.command
def runserver(*args, **kwargs):
  """Starts the server."""
  app = init_webapp()
  app.config_obj = config
  app.run(debug=True)


if __name__ == '__main__':
  manager.run()
