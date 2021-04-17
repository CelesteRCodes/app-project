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

names = ['Alan', 'Bernice', 'Charlie', 'Derrica', 'Selene', 
        'Zuri', 'Shannon', 'Malcolm', 'Jessie', 'Noel', 'Nat', 'Nadine']

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

temps = ["45", "50-55", "60-65", "70-75", "80-85", "90"]

water_level = ["0.5-1mL", "2-3mL", "4-5mL", "6-9mL", "10-15mL"]

nutes = ["0.5-1mL", "2-3mL", "4-5mL", "6-9mL", "10-15mL"]

humidity_list = ["30-35%", "40-45%", "50-55%", "60-65%", "70-75%", "80-85%"]

timestamps = ["13:33", "16:16", "12:22", "14:44", "11:11", "15:55"]

# username = 'soandso'
# email = 'soandso@gmail.com'
# password = '12345'
# so apparently, the user 'soandso' does exist, 
# was getting an error after running seed.py trying to hard code it in
# create new user function is working 


for n in range(10):
    email = f'user{n}@test.com'  
    password = 'test'
    username = f'username{n}'
    # variables to pass into CRUD.create_user

    user = CRUD.create_user(username, email, password)
    # creates the user (db.session.add/commit in CRUD.py)

    plant_type = choice(plants)
    # randomly chooses a plant
    
    plant_name = choice(names)

    plant = CRUD.create_plant(user.id, plant_name, plant_type)
    # creates the plant for user

    # photo_url = photo_urls[plant_choice]
    # can key into photo_url using plant_choice 

    new_entry = CRUD.create_entry(users_plant_id=users_plant_id, 
        comment=comments, timestamp=timestamps, water=water_level, 
        nutrients=nutes, temp=temps, humidity=humidity_list, photo_url=photo_urls)
    
    # db.session.commit()
    # creates the new entry for grow log



# logs = GrowLog.query.filter_by(id=id).order_by(desc(timestamp)).all()
# shows us the growlog by most recent posting first (descending order)