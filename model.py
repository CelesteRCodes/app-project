from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!

class users(db.Model):
    """Users table."""

    __tablename__ = "users"

    id = db.Column(db.Integer, # should this be plant_id or id? 
                       primary_key=True,
                       autoincrement=True,
                       )
    user_name = db.Column(db.String(50), nullable=False, unique=True,)
    email = db.Column(db.String(50), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False, unique=True,)
    

class userPlants(db.Model):
    """Plants table."""

    __tablename__ = "plants"

    id = db.Column(db.Integer, # should this be plant_id or id? 
                       primary_key=True,
                       autoincrement=True,
                       )

    user_id = db.Column(db.Integer, 
                        foreign_key=True,
                        autoincrement=True,
                        )
    plant_name = db.Column(db.String(50), nullable=False, unique=True,)
    photo_url = db.Column(db.) # unsure of how to code in a table for image information, is a string for the url?


class growLogs(db.Model):
    """Grow log table."""

    __tablename__ = "growlog"

    id = db.Column(db.Integer, 
                       primary_key=True,
                       autoincrement=True,
                       )
    users_plant_id = db.Column(db.Integer,
                       foreign_key=True,
                       autoincrement=True,
                       )
    plant_name = db.Column(db.String(50), nullable=False, unique=True,)
    photo_url = db.Column(db.(), nullable=True,) 
    # unsure of how to code in a table for image information, is a string for the url?
    # new photo for each entry; not pulling from user_plants' photo_url
    comment = db.Column(db.String(200), nullable=True,)


 

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