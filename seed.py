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

plants = ['aloe', 'ginger', 'bamboo', 'spider plant', 'sage', 'lavendar', 
        'tomato', 'orchid', 'avocado tree', 'spinach', 'cucumber', 'celery']


comments = ["watered with ph water and no nutrients",
            "added nutrients",
            "pruned dead leaves",
            "repotted plant",
            "hardened off seedling",
            "cleaned leaves with soap and water",
            "moved location of plant to south window",
            "used new soil recipe (recipe here)",
            "overwatered so I'm withholding until dry",
            "named this one: Nadine",
            "added amethyst to soil",
            "added citrine to soil"]

images = ["/static/aloe.jpg",
              "/static/bamboo.jpg",
              "/static/ginger.jpg",
              "/static/spiderplant.jpg",
              "/static/lavendar.jpg",
              "/static/orchid.jpg",
              "/static/sage.jpg",
              "/static/tomato.jpg",
              "/static/avocado.jpg",
              "/static/celery.jpg",
              "/static/spinach.jpg",
              "/static/cucumber.jpg"]

for n in range(10):
    email = f'user{n}@test.com'  
    password = 'test'
    user_name = f'user_name{n}'
    
    user = CRUD.create_user(user_name, email, password)
    plant = CRUD.create_plant(user.id, choice(plants))
    # new_entry = CRUD.create_entry(user.id, choice(images))

# logs = GrowLog.query.filter_by(id=id).order_by(desc(timestamp)).all()
# shows us the growlog by most recent posting first (descending order)