

# Grow Better
See Where You’ve Been To See How You Grow <br>

![Grow Better](https://github.com/CelesteRCodes/app-project/blob/main/static/img/logo.jpg) 

# <a name="table-contents">
# Table of Contents
* [About Me](#about-me)
* [Description](#description)
* [Features](#features)
* [Technologies](#tech)
* [Installation](#install)
* [Support](#support)
* [Coming Soon](#comming-soon)
* [Release History](#release-history)


# <a name="about-me">
# About Me
Celeste is an ICU RN of 5 years, who recently found out that she's in love with computer programming. After facing burnout from working 12 hr shifts on the floors during these trying times, she finally decided to make a career change. Being a lifelong learner, jumping into a completely new field was actually enticing for this one. She enjoys adding new skills to her toolbelt and "I learn something new everyday," is one of her favorite sayings. <br><br>
Programming allows her to continue using that curious/solution oriented mindset every day. It also allows for "rubber-ducking" or "thinking outloud," which turned out to be a pleasant surprise for her, since this is one of her innate talents.<br><br>
Having the opportunity to create an app that she's been itching to make with assistance from talented instructors, is probably the best part of all. Grow Better came from a place of personal need. Her OCD struck her while gardening and created a desire for a log to store detailed documentation neatly with photos. So, Grow Better was born!  </a> <br><br>
[Table Of Contents](#table-contents)

# <a name="description">
# Description
Grow Better is a web app where users can log data, including photos, to document every step of their plant's growth. The idea is for the user to learn from past mistakes/mishaps and have the opportunity to watch their grow in real time with photo documentation. "See where you've been to see how you grow." Users can learn from trial and error with the logs to reference in the future as needed. 
</a><br><br>
[Table Of Contents](#table-contents)

# <a name="feautures">
# Features

**Homepage**
Users can register, login or retrieve login information from forgot password 


![Homepage](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/homepage.jpg)   

**Add New User**
Registers new user and creates a new database for user to add/update plants and their logs 
 

![Add New User](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/newuser.jpg) 

**Forgot Password**
Form where user enters login retrieval information to receive an email to change password 


![Forgot PW](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/forgotpw.jpg) 

**Show User's Plants**
Has links for each specific plant to: show plant's detail page, show the plant's log, and to update the plant's log
Can also add a new plant to the user's plants list 

![User's Plants](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/userplants.jpg)

**Add New Plant**
Adds a new plant to user's plant's page 
 

![Add New Plant](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/newplant.jpg) 

**Add New Entry**
Updates a specific plant log 


![New Entry](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/newentry.jpg) 

**Show Plant's Log**
Shows all entries for each specific plant 


![Show Plantlog](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/plantlog.jpg) 

**Show The Master Growlog**
For admin to view all logs submitted by all users 


![Master Growlog](https://github.com/CelesteRCodes/app-project/blob/main/static/img/printscreen/masterlog.jpg) 

</a><br>
[Table Of Contents](#table-contents)


# <a name="tech">
# Technologies Used
* Python
* HTML
* CSS
* SQLAlchemy (Database)
* Jinja2
* PostgresQL
* API Used:
    * Cloudinary Media Optimizer

</a><br>
[Table Of Contents](#table-contents)

# <a name="install">
# Installation
* To clone/fork this repo:
    * https://github.com/CelesteRCodes/app-project.git
* Create and activate a virtual environment inside your project directory:
    * virtualenv env
    * source env/bin/activate
* Install the dependencies:
    * pip3 install -r requirements.txt
* Sign up to use the [Cloudinary API](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Abrand&utm_content=507572878502&utm_term=cloudinary%20api&gclid=Cj0KCQjwvr6EBhDOARIsAPpqUPFrfsru9mbQuY89JR800DOLyWVIOvPx-99ZvFboVEupJBZ3Br41S7AaAgzgEALw_wcB) 
* Save your API keys in a file called secrets.sh:
    * export CLOUDINARY_KEY="YOUR_KEY"
    * export CLOUDINARY_SECRET="YOUR_SECRET"
* Source your keys from your secrets.sh file into your virtual environment:
    * source secrets.sh
* Set up the database:
    * python3 model.py
    * python3 seed.py
* Run the app:
    * python3 server.py
Can now navigate to 'localhost:5000/' to access Grow Better
    
</a><br>
[Table Of Contents](#table-contents)


# <a name="support"> 
# Support
Feel free to email me with any questions at: celestercodes@gmail.com 
</a><br><br>
[Table Of Contents](#table-contents)

# <a name="coming-soon">
# Coming Soon
* Problems/issues page: where users can add/view/edit (resolve) a list of problems for each plant.
This page will create an alert that will be displayed on user-plants.html until user resolves the issue
* Set up a resource page with links/information on specific plant types for users to gather more information for their grows on user-plants.html
* Set up a snapshot of most recent updates to plant-log.html that will be displayed on user-plants.html
* Set up a weekly summary snapshot from data entered into each plant-log.html to be displayed on plant-details.html 
* Make all snapshots easily "shareable" 
</a><br><br>
[Table Of Contents](#table-contents)

# <a name="release-history">
# Release History
![GrowBetter-Beta](https://img.shields.io/badge/GrowBetter-0.1.0-evergreen.svg) 
* Initial release of MVP (5/13/2021)
</a><br><br>
[Table Of Contents](#table-contents)


# Project Status
Currently Updating Project

# Acknowledgments
Hackbright Staff 


# License
This project is licensed under the terms of the MIT license. <br>
Copyright 2021, Celeste Rowe, All rights reserved.

