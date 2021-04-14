from flask import Flask, render_template, request, redirect, session

import flash

import CRUD
import model
import os



app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

# API_KEY = os.environ['TICKETMASTER_KEY']

# # not sure I need an API for this part; 
# # using one to gather info from Trefle for references
# # for sprint 2 

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

# # should just have the log in on the homepage,
# # after user logs in, it takes them to the input form page
# # after submitting input (user can skip this step, 
# # may need a 'skip' button),
# # the user's grow log with all entries is shown

@app.route('/login', methods=['POST'])
def show_login():
    """ Show login for user on homepage."""

    username = request.form.get('username')
    password = request.form.get('password')
    user = CRUD.get_user_by_username(username)
    


    
    if user and password == user.password:
        session["id"] = user.id
        redirect('/show-form')
    else:
        redirect('/homepage') 
# do i need to store the user's password/username first
# to be able to compare to what the user inputs for the login?
# need to query into database for email given, if object with email, 
# grab password and compare it to password given


@app.route('/show-form', methods=['GET'])
def show_input_form():
    """ Show form."""

    return render_template("/input-form.html")
   

# want to be able to take in a new username/pw 
# and ask if user wants to create a new account

# will have one route to show the form
# another to process the form

# @app.route('/login', methods=['POST'])
# def register_user():
#     """Create a new user."""

#     username = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')

#     user = CRUD.get_user_by_email(email)
    
#     if user:
#         flash('Cannot create an account with that email. Try again.')
#     else:
#         CRUD.create_user(username, email, password)
#         flash('Account created! Please log in.')

#     return redirect('/')


@app.route('/process-form', methods=['POST'])
def process_input_form():
   
    """Create a new entry."""
    if "id" in session:
        id = session["id"]
        users_plant_id = CRUD.get_user_by_id(id)

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


@app.route('/grow-log', methods=['GET'])
def display_growlog():
    """Show user's grow log."""

    

    return render_template("/grow-log.html")


# have to query the db for all the user's growlogs 
# and then use jinja to display them on grow-log

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')



# homepage where user logs in 
# entry page 
# grow log page that displays all entries in descending order (most recent first)