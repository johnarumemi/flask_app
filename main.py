from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)
# alternate is app.config["DEBUG"] = True to specify each variable manually

# We now also initialize our SQLAlchemy db
db = SQLAlchemy(app)

# region Classes to Interact with Tables in Database

class User(db.Model):
    # If you do not pass in tablename, SQLAlchemy sets tablename to lowercase of classname
    __tablename__ = "user_table"
    # These are the columns that describe the users table of the database
    id = db.Column(db.Integer(), primary_key=True)  # Integer Primary key. dunno if it has sequence or Serial
    # if you do not pass in column names, SQLAlchemy will assume name is same as variable name
    username = db.Column('username',db.String(255))
    password = db.Column('password', db.String(255))    # these var varying character (255)

    # Note, if the Database column is integer, passing in Booleans wil be converted to 0 and 1
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)
# endregion


@app.route('/')
def home():
    return "<h1>Hello World!</h>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

