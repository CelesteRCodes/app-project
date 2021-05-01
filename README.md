# Grow Better
See Where You’ve Been To See How You Grow

# Description
A web app where users can log data, including photos, to document every step of their plant's growth. The idea is for the user to learn from past mistakes/mishaps and have the opportunity to watch their grow in real time with photo documentation. Users can learn from trial and error with the logs to reference in the future as needed. 

# About Me
Celeste is an ICU RN of 5 years, who recently found out that she's in love with computer programming. After facing burnout from working 12 hr shifts on the floors during these trying times, she finally decided to make a career change. Being a lifelong learner, jumping into a completely new field was actually enticing for this one. She enjoys adding new skills to her toolbelt and "I learn something new everyday," is one of her favorite mantras. 
Programming allows her to continue using that curious/solution focused mindset every day. It also allows for "rubber-ducking" or "thinking outloud," which turned out to be a pleasant surprise for her, since this is one of her innate talents. Having the opportunity to create an app that she's been itching to make with assistance from talented instructors, is probably the best part of all. Grow Better came from a place of personal need. Her OCD struck her while gardening and created a desire for a log to store detailed documentation neatly with photos. So, Grow Better was born!    

# Visuals

# API Used
Cloudinary Media Optimizer

# Technologies Used
* Python
* HTML
* CSS
* SQLAlchemy (Database)
* Jinja2
* PostgresQL

# Installation
* git clone https://github.com/CelesteRCodes/app-project.git
* Virtual Studio (version control)
* pip3 install requirements.txt
* source env/bin/activate (work in virutal environment)
* source secrets.sh (for Cloudinary API)

# Usage

# Support 
Feel free to email me with any questions at: celestercodes@gmail.com 

# Features
* Log In (homepage.html)
* Add New User Form page; registers new user and creates new database for user to add/update plants their (new-user.html)
* Forgot Password Form page; user enters login retrieval information to receive an email to change password (forgotpw.html)
* User's Plants shows all plants added by user with links to show specific plant's log, update log; can also add a new plant (user-plants.html)
    * where you can update/view plant log, and plant details for each specific plant
* New Plant Form page to add a new plant to user's plant's page (new-plant.html)
* New Entry Form page to update specific plant log (new-entry.html)
* Plant log on plant-log.html; shows all entries for each specific plant (plant-log.html)
* Master Grow Log page for admin to view all logs submitted by all users (growlog.html)

# Roadmap
Coming Soon:
* Problems/issues page: where users can add/view/edit (resolve) a list of problems for each plant.
This page will create an alert that will be displayed on user-plants.html until user resolves the issue
* Set up a resource page with links/information on specific plant types for users to gather more information for their grows on user-plants.html
* Set up a snapshot of most recent updates to plant-log.html that will be displayed on user-plants.html
* Set up a weekly summary snapshot from data entered into each plant-log.html to be displayed on plant-details.html 
* Make all snapshots easily "shareable" 

# Authors and Acknowledgment
Hackbright Staff 

# License
This project is licensed under the terms of the MIT license.
Copyright 2021, Celeste Rowe, All rights reserved.

# Project Status
Currently Updating Project

# Release History
0.1.0 beta - Initial release of MVP
