
import os

from setuptools import setup

README = None
with open(os.path.abspath('README.md')) as fh:
  README = fh.read()

setup (
    name='flask_framework',
    version='0.1',
    description=README,
    author='Troy Holsapple',
    author_email='troy.holsapple@gmail.com',
    url='http://www.flask.com',
    packages=['flask_framework'],
    install_requires=[
      'Flask>=0.10.1',
      'configobj',
      'Flask-SQLAlchemy'
      ]
)
