from flask import Flask, render_template, request, redirect, session
import cloudinary.uploader

from datetime import datetime

from jinja2 import StrictUndefined

import flash

import CRUD
import model
import os

app = Flask(__name__)
CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_KEY_SECRET = os.environ['CLOUDINARY_SECRET']
app.secret_key = 'asldkfj;aslfjd;lj'


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def show_login():
    """ Show login for user on homepage."""

    username = request.form.get('username')
    password = request.form.get('password')
    user = CRUD.get_user_by_username(username)
    
    if user and password == user.password:
        session["id"] = user.id
        return redirect(f'/show-user-plants/{user.id}')
    else:
        return redirect('/') 

        

@app.route('/show-forgotpw', methods=['GET', 'POST'])
def show_forgotpw():
    """ Show form to retrieve user's info."""

    return render_template("/forgotpw.html")


@app.route('/process-forgotpw', methods=['GET', 'POST'])
def process_forgotpw():
    """ Process new user form."""
    
    # if "email" in session:
    #     email = session["email"]
    #     user_email = CRUD.get_user_by_email(email)
    #     if user_email == None:
    #         return redirect("/")
    
    return redirect("/")


@app.route('/show-new-user-form', methods=['GET', 'POST'])
def show_new_user_form():
    """ Show form to create a new user."""

    return render_template("/new-user.html")


@app.route('/process-new-user-form', methods=['GET', 'POST'])
def process_new_user_form():
    """ Process new user form."""

    if "username" not in session:
        

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        CRUD.create_user(username, email, password)
    
    return redirect("/login")


@app.route('/show-user-plants/<int:user_id>', methods=['GET'])
def show_user_plants(user_id):
    """ Show user's plants."""

    user_plants = CRUD.get_user_plants_by_user_id(user_id)

    return render_template("/user-plants.html", user_plants=user_plants)


@app.route('/plant-details/<int:id>', methods=['GET'])
def show_plant_details(id):

    plant = CRUD.get_plant_by_plant_id(id)

    return render_template('plant-details.html', plant=plant)


@app.route('/show-new-plant-form', methods=['GET', 'POST'])
def show_new_plant_form():
    """ Show form for a new plant."""

    return render_template("/new-plant.html")


@app.route('/process-new-plant-form', methods=['POST'])
def process_new_plant_form():
   
    """Add a new plant to user-plants.html"""

    if "id" in session:
        user_id = session["id"]
        
        plant_name = request.form.get('plant_name')
        plant_type = request.form.get('plant_type')
        germinate_date = request.form.get('germinate_date')
        directsow = request.form.get('directsow')
        transplant_date = request.form.get('transplant_date')
        growing_medium = request.form.get('growing_medium')
        location = request.form.get('location')
        environment = request.form.get('environment')
        lighting = request.form.get('lighting')
        schedule = request.form.get('schedule')

        my_file = request.files['my-file']
        print(my_file)
        if my_file.filename != "":

            result = cloudinary.uploader.upload(my_file, api_key=CLOUDINARY_KEY,
                                                api_secret=CLOUDINARY_KEY_SECRET,
                                                cloud_name='celestercodes')
            img_url = result['secure_url']
        else:
            img_url = None

        plant = CRUD.create_plant(user_id, plant_name=plant_name, plant_type=plant_type, germinate_date=germinate_date,
                    directsow=directsow, transplant_date=transplant_date, growing_medium=growing_medium,
                     location=location, environment=environment, lighting=lighting, schedule=schedule, photo_url=img_url)

        return redirect(f'/show-user-plants/{user_id}')
    


@app.route('/show-new-entry-form/<int:plant_id>')
def show_specific_plant_entry_form(plant_id):
    """Show the post with the given id, the id is an integer."""
    
    return render_template("/new-entry.html", plant_id=plant_id)


@app.route('/process-new-entry-form/<int:plant_id>', methods=['POST'])
def process_new_entry_form(plant_id):
   
    """Create a new entry."""
    if "id" in session:
        id = session["id"]

        comment = request.form.get('comment')
        # timestamp = request.form.get('timestamp')
        timestamp = datetime.now()
        water = request.form.get('water')
        nutrients = request.form.get('nutrients')
        nute_type = request.form.get('nute_type')
        temp = request.form.get('temp')
        humidity = request.form.get('humidity')
        my_file = request.files['my-file']
        print(my_file)
        if my_file.filename != "":

            result = cloudinary.uploader.upload(my_file, api_key=CLOUDINARY_KEY,
                                                api_secret=CLOUDINARY_KEY_SECRET,
                                                cloud_name='celestercodes')
            img_url = result['secure_url']
        else:
            img_url = None
        
        print(img_url)
        CRUD.create_entry(plant_id, comment, timestamp, 
            water=water, nutrients=nutrients, nute_type=nute_type, 
            temp=temp, humidity=humidity, photo_url=img_url)

        return redirect(f'/plant-log/{plant_id}')
    


@app.route('/plant-log/<int:plant_id>', methods=['GET'])
def show_plant_log(plant_id):
    """Show user's plant log."""

    plantlogs = CRUD.get_entries_by_plant_id(plant_id)

    return render_template("plant-log.html", plantlogs=plantlogs)



@app.route('/grow-log', methods=['GET', 'POST'])
def display_growlog():
    """Show user's grow log."""

    entries = CRUD.get_all_entries()

    return render_template("grow-log.html", entries=entries)


if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')
