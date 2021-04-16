from flask import Flask, render_template, request, redirect, session

import flash

import CRUD
import model
import os

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'


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
        return redirect('/login') 

# login should take user to their plant's page (DONE)
# that shows all of the user's plants (don't know how 
# to display inputted plants from user, maybe a dictionary?)

# each plant should be clickable, (could have a button under 
# plant or make the actual plant name a link for user)

# take user to the input new entry form for that 
# specific plant

@app.route('/show-new-user-form', methods=['GET', 'POST'])
def show_new_user_form():
    """ Show form to create a new user."""

    return render_template("/new-user.html")

@app.route('/process-new-user-form', methods=['GET', 'POST'])
def process_new_user_form():
    """ Process new user form."""

    if "email" in session:
        email = session["email"]

        # user_id = CRUD.get_user_id_by_id(id)

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        
        CRUD.create_user(username, email, password)
        flash("You Are In!")
    

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

        # user_id = CRUD.get_user_id_by_id(id)

        user = CRUD.get_user_by_id(id)  
        # this is picking the entire user profile

# changing CRUD.py to have 
# def get_user_id_by_id(id):
#   return User.query.filter_by(id=id).one()
#  can change user_id = CRUD.get_id_by_id
        # is there a way to pick just the user's id 
        # and not everything attached to the user's id?

        plant_name = request.form.get('plant_name')
        plant_type = request.form.get('plant_type')

        
        CRUD.create_plant(user.id, plant_name, plant_type)
        flash('New plant added!')


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

        # users_id = CRUD.get_user_by_id(id)

        users_plant_id = CRUD.get_user_by_id(id)  
        # this is picking the entire user profile

        # is there a way to pick just the user's id 
        # and not everything attached to the user's id?

# changing CRUD.py to have 
# def get_user_id_by_id(id):
#   return User.query.filter_by(id=id).one()
#  can change user_id = CRUD.get_id_by_id
        # is there a way to pick just the user's id 
        # and not everything attached to the user's id?


        comment = request.form.get('comment')
        timestamp = request.form.get('timestamp')
        water = request.form.get('water')
        nutrients = request.form.get('nutrients')
        temp = request.form.get('temp')
        humidity = request.form.get('humidity')
        
        
        photo_url = request.form.get('photo_url')
    
    
        if comment == None:
            flash('No new updates?')
        else:
            CRUD.create_entry(users_plant_id=users_plant_id, comment=comment, timestamp=timestamp, 
                water=None, nutrients=None, temp=None, humidity=None, photo_url=None)
            flash('New entry created! Click submit to see log.')

    # do i need an if statement so user doesn't have to input an entry, they can skip
    # or just a skip button in JS

        return redirect('/grow-log')
    else: 
        return redirect('/homepage')

## on 4/15: currently getting a TypeError: 'module' 
# object is not callable
 
@app.route('/grow-log', methods=['GET', 'POST'])
def display_growlog():
    """Show user's grow log."""

    

    return render_template("/grow-log.html")


# have to query the db for all the user's growlogs 
# and then use jinja to display them on grow-log?

if __name__ == '__main__':
    app.debug = True
    model.connect_to_db(app)
    app.run(host='0.0.0.0')



# homepage where user logs in 
# entry page 
# grow log page that displays all entries in descending order (most recent first)