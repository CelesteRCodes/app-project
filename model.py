from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """Users table."""

    __tablename__ = "users"

    id = db.Column(db.Integer,  
                       primary_key=True,
                       autoincrement=True,
                       )
    username = db.Column(db.String(50), nullable=False, unique=True,)
    email = db.Column(db.String(100), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False,)
    
# making the class User and Users table
# id is the primary key, it autoincrements with each new user
# column names = id, user_name, email, password
# only user_name and email have to be unique
# all columns must have values, no NULL

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
    plant_type = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    germinate_date = db.Column(db.String(50), nullable=True)
    directsow = db.Column(db.String(50), nullable= True)
    transplant_date = db.Column(db.String(50), nullable=True)
    growing_medium = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(50), nullable=True)
    environment = db.Column(db.String(50), nullable=True)
    lighting = db.Column(db.String(50), nullable=True)
    schedule = db.Column(db.String(50), nullable=True)

    user = db.relationship("User", backref = "plants")

# making the class UserPlant and plants table
# id is the primary key, it autoincrements with each new plant
# user_id is the foreign key that connects UserPlant to User
# using backref to create relationship between the 2 tables
# and saving that relationship in a variable, user


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
    water= db.Column(db.String, nullable=True)
    nutrients = db.Column(db.String, nullable=True)
    nute_type = db.Column(db.String, nullable=True)
    organic = db.Column(db.String, nullable=True)
    temp = db.Column(db.String, nullable=True)
    humidity = db.Column(db.String, nullable=True)
    photo_url = db.Column(db.String, nullable=True)
    
    userplants = db.relationship("UserPlant", backref = "growlogs")

# making the class GrowLog and growlogs table
# id is the primary key, it autoincrements with each new plant
# users_plant_id is the foreign key that connects GrowLog to UserPlant
# using backref to create relationship between the 2 tables
# and saving that relationship in a variable, userplants



def connect_to_db(flask_app, db_uri='postgresql:///project', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    
