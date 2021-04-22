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

users_plant_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

germinate_dates = []

directsow=n = []

transplant_dates = [] 

growing_mediums = []

locations = []

environments = []

lights = []


for n in range(10):
    
    comment = choice(comments)

    timestamp = choice(timestamps)

    water = choice(water_level)

    nutrients = choice(nutes)

    humidity = choice(humidity_list)

    temp = choice(temps)

    users_plant_id = choice(users_plant_ids)

    photo_url = choice(photo_urls)

    new_entry = CRUD.create_entry(users_plant_id=users_plant_id, comment=comments, 
        timestamp=timestamps, water=water_level, 
        nutrients=nutes, temp=temps, humidity=humidity_list, photo_url=photo_urls)

for n in range(10):

    plant_type = choice(plants)
    # randomly chooses a plant
    
    plant_name = choice(names)

    users_plant_id = choice(users_plant_ids)
    photo_url = choice(photo_urls)

    germinate_date = choice(germinate_dates)

    directsow = choice(directsows)
    transplant_date = choice(transplant_dates)
    growing_medium = choice(growing_mediums)
    location = choice(locations)
    environment = choice(environments)
    lighting = choice(lights)
    

    new_plant = CRUD.create_plant(user_id=user_id, plant_name=plant_name, 
            plant_type=plant_type, germinate_date=germinate_date,
            directsow=directsow, transplant_date=transplant_date, 
            growing_medium=growing_medium, location=location,
            environment=environment, lighting=lighting)


for n in range(10):
    email = f'user{n}@test.com'  
    password = 'test'
    username = f'username{n}'
    # variables to pass into CRUD.create_user

    
    user = CRUD.create_user(username=username, email=email, password=password)

    
    
# datetime.strptime([growlog'timestamp'], '%Y-%m-%d')
# is this correct to get a timestamp of current time from user's input?

    # db.session.commit()
    # creates the new entry for grow log



# logs = GrowLog.query.filter_by(id=id).order_by(desc(timestamp)).all()
# shows us the growlog by most recent posting first (descending order)