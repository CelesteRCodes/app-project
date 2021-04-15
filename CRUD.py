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

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
    
# test

# >>> get_user_by_username("celestercodes")

# <User 11>

def get_user_by_id(id):
    print(id)
    return User.query.filter_by(id = id).first()

# test

# >> get_user_by_id(11)

# <User 11>

def create_plant(user_id, plant_name, plant_type):
    plant = UserPlant(user_id=user_id, plant_name=plant_name, plant_type=plant_type)
    db.session.add(plant)
    db.session.commit()
    return plant

# test

# >>> create_plant(1, "Nadine")

# ...COMMIT
# <UserPlant 11>

def get_all_plants():
    return UserPlant.query.all()

def get_plant_by_id(id):
    return UserPlant.query.filter_by(id = id).first()

# test

# >>> get_plant_by_id(3)

# <UserPlant 3>

def create_entry(users_plant_id, comment, timestamp, water=None, nutrients=None, temp=None, 
    humidity=None, photo_url=None):
    new_entry = GrowLog(users_plant_id=users_plant_id, comment=comment, timestamp=timestamp, water=water, nutrients=nutrients, temp=temp, 
        humidity=humidity, photo_url=None)
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

def get_entry_by_id(id):
    return GrowLog.query.filter_by(id = id).first()

# test
# >>> get_entry_by_id(2)

# <GrowLog2>

if __name__ == '__main__':
    from server import app
    connect_to_db(app)



# create - post
# read - get
# update - put
# delete - delete