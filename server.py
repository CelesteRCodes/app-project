from flask import Flask, render_template, request, redirect

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

@app.route('/login')
def show_login():
    """ Show login for user on homepage."""

    username = request.form.get('username')
    password = request.form.get('password')

# do i need to store the user's password/username first
# to be able to compare to what the user inputs for the login?

    if username == 'user' and password == '12345':
        return render_template('input-form.html')
    else:
        return render_template('homepage.html')

# want to be able to take in a new username/pw 
# and ask if user wants to create a new account


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


@app.route('/input-form')
def show_input_form():
   
    """Create a new entry."""

    comment = request.form.get('username')
    timestamp = request.form.get('email')
    photo_url = request.form.get('password')

    users_plant_id = CRUD.get_user_by_id(id)
    
    if comment == None:
        flash('Nothing to add?')
    else:
        CRUD.create_entry(users_plant_id=users_plant_id, timestamp=timestamp, comment=comment, photo_url=None)
        flash('New entry created! Click submit to see log.')

    # do i need an if statement so user doesn't have to input an entry, they can skip
    # or just a skip button in JS

    return redirect('/grow-log.html')
    


@app.route('/grow-log')
def display_input():
    """Show user's grow log."""

    # keyword = request.args.get('keyword', '')
    
    # userplants = request.args.get('plants', '')
    growlogs = request.args.get('growlogs', '')
    

    url = 'grow-log.html'
    payload = {
            #  'keyword': keyword,
            #    'userplants': plants,
               'growlog': growlogs}

    response = request.get(url, params=payload)

    data = response.json()
    growlog = data['_embedded']['growlog']

    return render_template('grow-log.html',
                        #    pformat=pformat,
                        #    userplants=userplants,
                           data=data,
                           growlog=growlog)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')



# homepage where user logs in 
# entry page 
# grow log page that displays all entries in descending order (most recent first)