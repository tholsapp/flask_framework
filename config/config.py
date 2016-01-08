#!env/bin/python

import os

from configobj import ConfigObj

# Points to parent directory #
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

config = ConfigObj()

config.filename = 'config.py'


# the URI is required by flask-sqlalchemy extension. This is the path of the database file #
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# the REPO is where the migration files are stored #
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals.
# The default is None, which enables tracking but issues a warning that it will be disabled by default in the future.
# This requires extra memory and should be disabled if not needed. #
SQLALCHEMY_TRACK_MODIFICATIONS = True


""" Initialize Flask Configurations """

config['WTF_CSRF_ENABLED'] = True
config['SECRET_KEY'] = 'abc123'



