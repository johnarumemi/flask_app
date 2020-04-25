from main import app, db, User
import psycopg2

psycopg2._ext
# This allows us to work with the models in the Flask shell because we are injecting
# run db.create_all() in flask shell
# ensure you do > export FLASK_APP=manage.py first though
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)