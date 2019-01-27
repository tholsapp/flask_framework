#!env/bin/python

from app import app

@app.errorhandler(403)
def forbidden(error):
  return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def not_found_error(error):
  return render_template('500.html'), 500
