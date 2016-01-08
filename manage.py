#!env/bin/python

import os.path
import imp
from migrate.versioning import api
from configobj import ConfigObj

from flask.ext.script import Manager

from config import config, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import app, db, init_webapp

manager = Manager(app)




""" Start Server """
@manager.command
def runserver(*args, **kwargs):
  app = init_webapp()
  app.config_obj = config
  app.run(debug=True)



"""                     """
""" Database Management """
"""                     """

""" Create Dataabase """
@manager.command
def db_create():
  db.create_all()

  if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHMEY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
  else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

""" Migrate Database """
@manager.command
def db_migrate():
  v           = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
  migration   = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
  tmp_module  = imp.new_module('old_model')
  old_model   = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

  exec(old_model, tmp_module.__dict__)
  script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
  open(migration, "wt").write(script)
  api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
  v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

  print('New migration saved as ' + migration)
  print('Current database version: ' + str(v))

""" Upgrade Database """
@manager.command
def db_upgrade():
  api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
  v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

  print('Current database version: ' + str(v))

""" Downgrade Database """
@manager.command
def db_downgrade():
  v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
  api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
  v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

  print('Current database version: ' + str(v))

if __name__ == '__main__':
  manager.run()

