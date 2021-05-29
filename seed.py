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

photo_urls = ["\static\img\plant-images\aloe.jpg",
             "\static\img\plant-images\\bamboo.jpg",
              "\static\img\plant-images\ginger.jpg",
              "\static\img\plant-images\spiderplant.jpg",
              "\static\img\plant-images\lavendar.jpg",
              "\static\img\plant-images\orchid.jpg",
              "\static\img\plant-images\sage.jpg",
              "\static\img\plant-images\\tomato.jpg",
              "\static\img\plant-images\\avocado.jpg",
              "\static\img\plant-images\celery.jpg",
              "\static\img\plant-images\spinach.jpg",
              "\static\img\plant-images\cucumber.jpg"]

        
temps = ["45", "50-55", "60-65", "70-75", "80-85", "90"]

water_level = ["0.5-1mL", "2-3mL", "4-5mL", "6-9mL", "10-15mL"]

nutes = ["0.5-1mL", "2-3mL", "4-5mL", "6-9mL", "10-15mL"]

humidity_list = ["30-35%", "40-45%", "50-55%", "60-65%", "70-75%", "80-85%"]


plant_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

germinate_dates = ["01/10/2020", "02/02/2020", "03/03/2020", "04/04/2020", "05/05/2020"]

directsows = ["direct sown", "transplant"]

transplant_dates = ["01/11/2020", "02/12/2020", "03/13/2020", "04/14/2020", "05/17/2020"] 

growing_mediums = ["soil", "water only", "perlite", "rockwool", 
        "clay pebbles", "coco coir"]

locations = ["indoor", "outdoor"]

environments = ["grow tent/room", "cabinet greenhouse", "windowsill",
        "direct sow", "raised bed", "container", "greenhouse"]

lights = ["sunlight", "fluorescent", "led", "hps", "cfl"]

schedules = ["on mother nature's time", "12 on, 12 off", "6-10 on", "24 on"]

nute_types = ["eggshells", "banana water", "fish fertilizer", "compost tea", "rabbit/chicken poo"]

organic = ["Y", "N"]

for n in range(10):
    email = f'user{n}@test.com'  
    password = 'test'
    username = f'username{n}'
    # variables to pass into CRUD.create_user

    
    user = CRUD.create_user(username=username, email=email, password=password)

# function that creates 10 test users for the users table in model.py

for n in range(10):

    plant_type = choice(plants)
    # choice(plants) randomly chooses a plant
    
    plant_name = choice(names)
    

    user_id = choice(user_ids)
    plant_id = choice(plant_ids)
    photo_url = choice(photo_urls)

    germinate_date = choice(germinate_dates)

    directsow = choice(directsows)
    transplant_date = choice(transplant_dates)
    growing_medium = choice(growing_mediums)
    location = choice(locations)
    environment = choice(environments)
    lighting = choice(lights)
    schedule = choice(schedules)
    

    new_plant = CRUD.create_plant(user_id=user_id, plant_name=plant_name, 
            plant_type=plant_type, photo_url=photo_url, germinate_date=germinate_date,
            directsow=directsow, transplant_date=transplant_date, 
            growing_medium=growing_medium, location=location,
            environment=environment, lighting=lighting, schedule=schedule)

# function that creates 10 test plants for the plants table 


for n in range(10):
    
    comment = choice(comments)

    timestamp = datetime.now()

    water = choice(water_level)

    nutrients = choice(nutes)

    nute_type = choice(nute_types)

    organic = choice(organic)

    humidity = choice(humidity_list)

    temp = choice(temps)

    users_plant_id = choice(plant_ids)

    photo_url = choice(photo_urls)

    new_entry = CRUD.create_entry(users_plant_id=users_plant_id,
        comment=comment, timestamp=timestamp, water=water, 
        nutrients=nutrients, nute_type=nute_type, organic=organic, 
        temp=temp, humidity=humidity, photo_url=photo_url)


    # function creates 10 test entries for the growlog table