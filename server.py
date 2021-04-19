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

    if "email" in session:
        email = session["email"]

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        
        CRUD.create_user(username, email, password)
    
    return redirect("/login")


@app.route('/show-user-plants', methods=['GET', 'POST'])
def show_user_plants():
    """ Show user's plants."""

    return render_template("/user-plants.html")

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
    

@app.route('/show-new-entry-form', methods=['GET', 'POST'])
def show_new_entry_form():
    """ Show form for a new entry/update log of a plant."""

    return render_template("/new-entry.html")
   


@app.route('/process-new-entry-form', methods=['GET', 'POST'])
def process_new_entry_form():
   
    """Create a new entry."""
    if "id" in session:
        id = session["id"]

        users_plant_id = CRUD.get_user_plant_by_id(id)  
        

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

        return redirect('/grow-log')
    else: 
        return redirect('/homepage')

 
@app.route('/grow-log', methods=['GET', 'POST'])
def display_growlog():
    """Show user's grow log."""

    # users_plant_id = CRUD.get_user_plant_by_id(id)

    entries = CRUD.get_all_entries()

    # return render_template("/grow-log.html", users_plant_id=users_plant_id.user_id, 
    # comment=comment, timestamp=datetime.now(), water=None, nutrients=None, 
    # temp=None, humidity=None, photo_url=None)

    return render_template("/grow-log.html", entries=entries)

# have to query the db for all the user's growlogs 
# pass info in return render_template for growlog
# and then use jinja to display them on grow-log?


if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')



# homepage where user logs in 
# entry page 
# grow log page that displays all entries in descending order (most recent first)