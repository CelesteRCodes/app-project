from model import User, UserPlant, GrowLog, db, connect_to_db


def create_user(username, email, password):
    user = User(username = username, 
        email = email, password = password)
    
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.all()

def get_user_by_username(username):
    return User.query.all()

def get_user_by_id(id):
    return User.query.filter_by(id = id).first()

def create_plant(user_id, plant_name):
    plant = UserPlant(user_id=user_id, plant_name=plant_name)
    db.session.add(plant)
    db.session.commit()
    return plant

def get_all_plants():
    return UserPlant.query.all()

def get_plant_by_id(id):
    return UserPlant.query.filter_by(id = id).first()


def create_entry(users_plant_id, timestamp, comment=None, photo_url=None):
    new_entry = GrowLog(users_plant_id=users_plant_id, timestamp=timestamp, 
        comment=comment, photo_url=photo_url)
    db.session.add(new_entry)
    db.session.commit()
    return new_entry

def get_all_entries():
    return GrowLog.query.all()

def get_entry_by_id(id):
    return GrowLog.query.filter_by(id = id).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)



# create - post
# read - get
# update - put
# delete - delete