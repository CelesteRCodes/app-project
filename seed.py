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

photo_urls = {"aloe": "/static/aloe.jpg",
             "bamboo": "/static/bamboo.jpg",
              "ginger":"/static/ginger.jpg",
              "spider plant":"/static/spiderplant.jpg",
              "lavendar":"/static/lavendar.jpg",
              "orchid":"/static/orchid.jpg",
              "sage":"/static/sage.jpg",
              "tomato":"/static/tomato.jpg",
              "avocado": "/static/avocado.jpg",
              "celery":"/static/celery.jpg",
              "spinach":"/static/spinach.jpg",
              "cucumber":"/static/cucumber.jpg"}

for n in range(10):
    email = f'user{n}@test.com'  
    password = 'test'
    username = f'username{n}'
    # variables to pass into CRUD.create_user

    user = CRUD.create_user(username, email, password)
    # creates the user (db.session.add/commit in CRUD.py)

    plant_choice = choice(plants)
    # randomly chooses a plant

    plant = CRUD.create_plant(user.id, plant_choice)
    # creates the plant for user

    photo_url = photo_urls[plant_choice]
    # can key into photo_url using plant_choice 

    new_entry = CRUD.create_entry(plant.id, datetime.now(), photo_url=photo_url)
    # creates the new entry for grow log




# logs = GrowLog.query.filter_by(id=id).order_by(desc(timestamp)).all()
# shows us the growlog by most recent posting first (descending order)