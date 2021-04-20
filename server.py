from flask import Flask, render_template, request, redirect, session
from datetime import datetime

from jinja2 import StrictUndefined

import flash

import CRUD
import model
import os

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def show_login():
    """ Show login for user on homepage."""

    username = request.form.get('username')
    password = request.form.get('password')
    user = CRUD.get_user_by_username(username)
    
    if user and password == user.password:
        session["id"] = user.id
        return redirect('/show-user-plants')
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

    if "username" in session:
        username = session["username"]

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        CRUD.create_user(username, email, password)
    
    return redirect("/login")

# new users are not being created, stored in db; no errors are thrown

@app.route('/show-user-plants', methods=['GET', 'POST'])
def show_user_plants():
    """ Show user's plants."""

    all_plants = CRUD.get_all_plants()

    return render_template("/user-plants.html", all_plants=all_plants)

@app.route('/show-new-entry-form/<int:id>')
def show_specific_plant_entry_form(id):
    """Show the post with the given id, the id is an integer."""

    return render_template("/new-entry.html")

# need to store id in a session to ensure that the entry 
# is being stored with that id
# when rendering template, show plant's name on top

@app.route('/show-new-plant-form', methods=['GET', 'POST'])
def show_new_plant_form():
    """ Show form for a new plant."""

    return render_template("/new-plant.html")


@app.route('/process-new-plant-form', methods=['GET', 'POST'])
def process_new_plant_form():
   
    """Add a new plant to user-plants.html"""

    if "id" in session:
        id = session["id"]

        user = CRUD.get_user_by_id(id)  
        
        plant_name = request.form.get('plant_name')
        plant_type = request.form.get('plant_type')
 
        CRUD.create_plant(user.id, plant_name, plant_type)

        return redirect('/show-user-plants')
    

@app.route('/process-new-entry-form', methods=['GET', 'POST'])
def process_new_entry_form():
   
    """Create a new entry."""
    if "id" in session:
        id = session["id"]

        users_plant_id = CRUD.get_user_plant_by_id(id)  
        # plant_id = CRUD.get_plant_id(id)  
        # should i change this to plant_id?

        comment = request.form.get('comment')
        timestamp = request.form.get('timestamp')
        # timestamp = datetime.now()
        water = request.form.get('water')
        nutrients = request.form.get('nutrients')
        temp = request.form.get('temp')
        humidity = request.form.get('humidity')
        photo_url = request.form.get('photo_url')
    
    
        if comment == None:
            flash('No new updates?')
        else:
            CRUD.create_entry(users_plant_id=users_plant_id.user_id, 
            comment=comment, timestamp=datetime.now(), 
            water=water, nutrients=nutrients, temp=temp, 
            humidity=humidity, photo_url=None)

        return redirect('/plant-log')
    else: 
        return redirect('/show-user-plants')

 
# @app.route('/plant-log/<int:id>')
# def display_plantlog(id):
#     """Show the post with the given id, the id is an integer."""

#     entries = CRUD.get_entry_by_id(id)

#     return render_template("plant-log.html", entries=entries)

# not showing page for plant log with id, throwing a 404 
# will show plant log without id, all the entries 

@app.route('/plant-log', methods=['GET', 'POST'])
def display_plantlog():
    """Show user's plant log."""

    entries = CRUD.get_all_entries()

    return render_template("plant-log.html", entries=entries)


@app.route('/grow-log', methods=['GET', 'POST'])
def display_growlog():
    """Show user's grow log."""

    entries = CRUD.get_all_entries()

    return render_template("grow-log.html", entries=entries)


if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')
