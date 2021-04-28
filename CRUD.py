from model import User, UserPlant, GrowLog, db, connect_to_db

from datetime import datetime


def create_user(username, email, password):
    user = User(username = username, email = email, password = password)
    
    db.session.add(user)
    db.session.commit()
    return user

# test

# >>> create_user("celestercodes", "celestercodes@gmail.com", "bestcoderever")

# ...COMMIT
# <User 11> new user is made

def get_all_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter_by(email=email).one()

# test

# >>> get_user_by_email("celestercodes@gmail.com")

# <User 11>


# def get_user_id_by_id(id):
#     return User.query.filter_by(id=id).one()


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
    
# test

# >>> get_user_by_username("celestercodes")

# <User 11>

def get_user_by_id(id):
    user_id = User.query.filter_by(id = id).first()
    
    return user_id

# test

# >> get_user_by_id(11)

# <User 11>

def create_plant(user_id, plant_name, plant_type, photo_url, germinate_date,
                    directsow, transplant_date, growing_medium, location,
                    environment, lighting, schedule):
    plant = UserPlant(user_id=user_id, plant_name=plant_name, 
            plant_type=plant_type, germinate_date=germinate_date,
            directsow=directsow, transplant_date=transplant_date, 
            growing_medium=growing_medium, location=location,
            environment=environment, lighting=lighting, schedule=schedule, photo_url=photo_url)
    db.session.add(plant)
    db.session.commit()
    return plant

# test

# >>> create_plant(1, "Nadine")

# ...COMMIT
# <UserPlant 11>

def get_all_plants():
    plants = UserPlant.query.all()
    return plants

# test:
#     
# get_All_plants()
# >>> [<UserPlant 1>, <UserPlant 2>, <UserPlant 3> 
# ... <<UserPlant 10>]


def get_plant_by_plant_id(id):
    plant_by_id = UserPlant.query.filter_by(id = id).first()
    
    return plant_by_id
    # user-plant object returned

    # >>> get_user_plant_by_id(3)
    # <UserPlant 3>

def get_user_plants_by_user_id(user_id):
    user_plants = UserPlant.query.filter_by(user_id=user_id).all()
    return user_plants

   # get_user_plants_by_user_id(5)
   # >>> [<UserPlant 3>, <UserPlant 7>, <UserPlant 10>]

def create_entry(users_plant_id, comment, timestamp, 
    water=None, nutrients=None, nute_type=None, temp=None, 
    humidity=None, photo_url=None):
    
    

    new_entry = GrowLog(users_plant_id=users_plant_id, 
        comment=comment, timestamp=timestamp, water=water, 
        nutrients=nutrients, nute_type=nute_type, temp=temp, 
        humidity=humidity, photo_url=photo_url)

    db.session.add(new_entry)
    db.session.commit()
    return new_entry

# test

# >>> create_entry(1, "leaves are green", datetime.now(), "1-5ml", "5-10ml", "70-75", "30-35%")

# ...COMMIT
# <GrowLog 12>

def get_all_entries():
    return GrowLog.query.all()

# test

# >>> get_all_entries()

# <GrowLog 1> ... <GrowLog12> shows all growlogs

def get_entries_by_plant_id(users_plant_id):
    return GrowLog.query.filter_by(users_plant_id = users_plant_id).all()


def get_entry_by_id(id):
    return GrowLog.query.filter_by(id = id).first()

# test
# >>> get_entry_by_id(2)

# <GrowLog2>


# to get entries for a specific plant, 
# use users_plant_id, the foreign key?

# def get_get_by_users_plant_id(id):
#     GrowLog.query.filter_by(users_plant_id=users_plant_id).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)



# create - post
# read - get
# update - put
# delete - delete