from flask import Flask, render_template, request

from pprint import pformat
import os
import requests


app = Flask(__name__)
# app.secret_key = 'SECRETSECRETSECRET'
# API_KEY = os.environ['TICKETMASTER_KEY']

# not sure I need an API for this part; 
# using one to gather info from Trefle for references
# for sprint 2 

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

# should just have the log in on the homepage,
# after user logs in, it takes them to the input form page
# after submitting input (can skip this step),
# the user profile is shown with the inputted data (another page)

@app.route('/inputform')
def show_input_form():
    """Show user input form."""

    return render_template('input-form.html')


@app.route('/inputform/display')
def display_input():
    """Show input from user."""

    # keyword = request.args.get('keyword', '')
    plant_types = request.args.get('plant types', '')
    user_plants = request.args.get('user plants', '')
    grow_log = request.args.get('grow_log', '')
    

    url = ''
    payload = {
            #    'keyword': keyword,
               'plantTypes': plant_types,
               'userPlants': user_plants,
               'growLog': grow_log}

    response = requests.get(url, params=payload)

    data = response.json()
    grow_log = data['_embedded']['grow_log']

    return render_template('.html',
                        #    pformat=pformat,
                           data=data,
                           grow_log=grow_log)

# should the input-form display just be the user profile (for first sprint)?


@app.route('/user-profile/<id>')
def get_user_profile(id):
    """View the user's profile."""

    url = f'{id}'
    payload = {}

    response = requests.get(url, params=payload)

    event = response.json()
    profile = event['_embedded']['profile']

    return render_template('user-profile.html',
                           event=event,
                           profile=profile)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
