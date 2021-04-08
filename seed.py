import os
from datetime import datetime
from random import choice, randint

import CRUD
import model
import server

os.system('dropdb project')
os.system('createdb project')
# creates and deletes databases

model.connect_to_db(server.app)
# runs like python3 model.py

model.db.create_all()
# creates db tables
plants = ['aloe', 'fern', 'barely', 'spiderplant', 'cacti', 'palm', 'cherry blossom', 'orchid']


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    user_name = f'user_name{n}'
    
    user = CRUD.create_user(user_name, email, password)
    plant = CRUD.create_plant(user.id, choice(plants))
# logs = GrowLog.query.filter_by(id=id).order_by(desc(timestamp)).all()