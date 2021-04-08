from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Replace this with your code!

class User(db.Model):
    """Users table."""

    __tablename__ = "users"

    id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=True,
                       )
    user_name = db.Column(db.String(50), nullable=False, unique=True,)
    email = db.Column(db.String(50), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False,)
    

class UserPlant(db.Model):
    """Plants table."""

    __tablename__ = "plants"

    id = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )

    user_id = db.Column(db.Integer, 
                        db.ForeignKey("users.id"),
                        )
    plant_name = db.Column(db.String(50), nullable=False)
    
    user = db.relationship("User", backref = "plants")


class GrowLog(db.Model):
    """Grow log table."""

    __tablename__ = "growlogs"

    id = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )
    users_plant_id = db.Column(db.Integer,
                       db.ForeignKey("plants.id")
                       )
    
    comment = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(db.DateTime)
    photo_url = db.Column(db.String, nullable=True)

    userplants = db.relationship("UserPlant", backref = "growlogs")

def connect_to_db(flask_app, db_uri='postgresql:///project', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)