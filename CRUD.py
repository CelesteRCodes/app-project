from model import User, UserPlant, GrowLog, db, connect_to_db

from datetime import datetime


def create_user(username, email, password):
    """ 
    For example:

    >>> create_user("celestercodes", "celestercodes@gmail.com", "bestcoderever")

    [<User 12>]
    """
    user = User(username = username, email = email, password = password)
    
    db.session.add(user)
    db.session.commit()
    return user

    # can have function that deletes user (for when they want to deactivate their profile)
    # will also have to ensure it deletes all the user's data in db like the plants/entries


def get_all_users():
    """ For example:
    >>> get_all_users()

    [<User 1>, <User 2>, <User 3>, <User 4>, <User 5>, <User 6>,
    <User 7>, <User 8>, <User 9>, <User 10>,<User 12>, <User 12>]
    """ 
    return User.query.all()

def get_user_by_email(email):
    """ For example:
    >>> get_user_by_email("celestercodes@gmail.com")

    [<User 12>]
    """ 
    return User.query.filter_by(email=email).one()



def get_user_by_username(username):
    """ For example:
    >>> get_user_by_username("celestercodes")

    [<User 12>]
    """ 
    return User.query.filter_by(username=username).first()


def get_user_by_id(id):
    """ For example:
    >>> get_user_by_id(11)

    [<User 11>]
    """ 
    user_id = User.query.filter_by(id = id).first()
    
    return user_id


def create_plant(user_id, plant_name, plant_type, photo_url, germinate_date,
                    directsow, transplant_date, growing_medium, location,
                    environment, lighting, schedule):
    """ For example:
    >>> create_plant(1, "Nadine", "Aloe", "/static/img/aloe.jpg", "11/11/2020", 
    "direct sow", "11/11/2020", "soil", "indoor", "windowsill", "sunlight", "mother natures time") 

    [<UserPlant 12>] 
    """ 

    plant = UserPlant(user_id=user_id, plant_name=plant_name, 
            plant_type=plant_type, germinate_date=germinate_date,
            directsow=directsow, transplant_date=transplant_date, 
            growing_medium=growing_medium, location=location,
            environment=environment, lighting=lighting, 
            schedule=schedule, photo_url=photo_url)
    db.session.add(plant)
    db.session.commit()
    return plant


def get_all_plants():
    """ For example: 
    >>> get_all_plants()

    [<UserPlant 1>, <UserPlant 2>, <UserPlant 3>, <UserPlant 4>, <UserPlant 5>, <UserPlant 6>, <UserPlant 7>,
    <UserPlant 8>, <UserPlant 9>, <UserPlant 10>, <UserPlant 11>, <UserPlant 12>] 
    """
    plants = UserPlant.query.all()
    return plants

# to combine all get_all functions
# pass in variable 
# def get_all_plants(n):
# value = (n).query.all()

def get_plant_by_plant_id(id):
    """ For example:
    >>> get_plant_plant_by_id(3)

    [<UserPlant 3>]
    """ 
    plant_by_id = UserPlant.query.filter_by(id = id).first()
    
    return plant_by_id
   
   # can also have function that deletes plant by plant ID
   # will remove this plant from plant-details.html and the db

def get_user_plants_by_user_id(user_id):
    """ For example:
    >>> get_user_plants_by_user_id(3)

   [<UserPlant 4>] 
   """ 
    user_plants = UserPlant.query.filter_by(user_id=user_id).all()
    return user_plants


def create_entry(users_plant_id, comment, timestamp, 
    water=None, nutrients=None, nute_type=None, organic=None, temp=None, 
    humidity=None, photo_url=None):
    """ For example:
    >>> create_entry(1, "leaves are green", datetime.now(), "1-5ml", 
    "5-10ml", "eggshells", "70-75", "30-35%", "/static/img/aloe.jpg")

    [<GrowLog 12>] 
    """ 

    new_entry = GrowLog(users_plant_id=users_plant_id, 
        comment=comment, timestamp=timestamp, water=water, 
        nutrients=nutrients, nute_type=nute_type, organic=organic, 
        temp=temp, humidity=humidity, photo_url=photo_url)

    db.session.add(new_entry)
    db.session.commit()
    return new_entry

# need to actually format datetime so it's adaptable to timezones per user

def get_all_entries():
    """ For example:
    >>> get_all_entries()
    [<GrowLog 1>, <GrowLog 2>, <GrowLog 3>, <GrowLog 4>, <GrowLog 5>, <GrowLog 6>, <GrowLog 7>,
    <GrowLog 8>, <GrowLog 9>, <GrowLog 10>, <GrowLog 11>, <GrowLog 12>] """ 
    return GrowLog.query.all()


def get_entries_by_plant_id(users_plant_id):
    """ For example:
    >>> get_entries_by_plant_id(4)
    [<GrowLog 4>]
    """
    return GrowLog.query.filter_by(users_plant_id = users_plant_id).all()

    # can also have function that deletes all entries by plant ID
    # which will clear the plant-log for that plant
    


def get_entry_by_id(id):
    """ For example:
    >>> get_entry_by_id(2)
    [<GrowLog2>] 
    """ 
    return GrowLog.query.filter_by(id = id).first()

# can also have function that deletes entry by ID



if __name__ == '__main__':
    from server import app
    connect_to_db(app)


    # $ python3 -m doctest CRUD.py to run doctests