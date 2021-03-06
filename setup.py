
import os

from setuptools import setup, find_packages


setup (
    name='flask-framework',
    version='0.0.1',
    description='Flask framework skeleton.',
    packages=find_packages(),
    install_requires=[
      'configobj>=5.0.*',
      'coverage>=4.5.*',
      'Flask>=1.0.*',
      'Flask-Bootstrap>=3.3.*',
      'Flask-Script>=2.0.*',
      'Flask-SQLAlchemy>=2.3.*',
      'pytest>=4.2.*',
      'pytest-cov==2.5.*',
      'sqlalchemy>=1.2.*',
      'sqlalchemy-migrate>=0.12.*',
      ],

    author='Troy Holsapple',
    author_email='troy.holsapple@gmail.com',
    url='http://www.flask.com',
    )
