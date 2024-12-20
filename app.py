from flask import Flask, redirect, render_template, request, url_for
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from operator import index
from flask import Flask, render_template
import datetime as dt
import pandas as pd
import pytz
from datetime import datetime, timezone
import time


load_dotenv()
app = Flask(__name__)
faq_dictionary = {}

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('APP_SECRET_KEY')


# Initialize SQLAlchemy
db = SQLAlchemy(app)

import psycopg2



class Contact(db.Model):
    __tablename__ = 'contacts'  # Ensure the table name matches your original schema

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    office_role = db.Column(db.String(50), nullable=False)  # New field

    def __repr__(self):
        return f'<Contact {self.name}>'

@app.route('/')
def index():

# Check if a search query exists in the request arguments
    search_query = request.args.get('searchbar', '')

# Set the timezone to 'America/New_York'
    timezone = pytz.timezone("America/New_York")
    
    # Get the current time in New York timezone (aware datetime)
    actual_date = datetime.now(timezone)
    
    # Target date for the countdown: June 11th, 2026, as aware datetime
    target_date = datetime(2026, 6, 11, 0, 0, 0, 0)
    target_date = timezone.localize(target_date)  # Make target_date aware by setting the timezone
    
    # Calculate the difference between target date and actual date
    time_remaining = target_date - actual_date

    # Get the number of days, hours, minutes, and seconds
    days_until = time_remaining.days
    hours_until = time_remaining.seconds // 3600
    minutes_until = (time_remaining.seconds % 3600) // 60
    seconds_until = time_remaining.seconds % 60

    if search_query:  # If the search query is not empty
        return render_template('oopsNotAvailable.html', search_query=search_query)
    else:  # If no search query is provided
        return render_template('index.html', days_until=days_until, hours_until=hours_until, 
                           minutes_until=minutes_until, seconds_until=seconds_until)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission (you can add form validation here if needed)
        
        # For now, just redirect to 'oopsNotAvailable.html'
        return redirect(url_for('oops_page'))
    
    # Render the login page for GET request
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Redirect to the 'oopsNotAvailable' page after form submission
        return redirect(url_for('oops_page'))
    
    # Render the signup page for GET request
    return render_template('signup.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form.get('name')
        email = request.form.get('email')
        office_role = request.form.get('office_role')  # Get the office_role field
        comments = request.form.get('comments')

        # Create a new Contact instance and add it to the database
        new_contact = Contact(name=name, email=email, office_role=office_role, comments=comments)

        # Add the new contact to the session and commit
        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('contact.html', contact_active=True)


@app.route('/about')
def info():
    faq_listofQuestions = ["What is FreeKick?", "What FreeKick offers?", "Is it true that I can stay up to date with the latest AI, tech, and soccer analytics?", \
        "Who runs FreeKick?","Is FreeKick a for or not-for profit organization?"]
    faq_listofAnswers = ["FreeKick is a club organization that looks to connect communites to the most immersive US 2026 World Soccer Analytics and AI experience. "  \
        ,"FreeKick provides services that engage the community with the biggest sporting event in the world, the 2026 World Cup.", "Yes FreeKick takes advantage of AI, soccer analytics, passionate 2026 World Cup enthusiasts to keep you updated." \
            , "We are group of students and young professionals." , "FreeKick is a student club with the goal of turning into an LLC service company."]  
    for i in range(5):
        faq_dictionary[faq_listofQuestions[i]] = faq_listofAnswers[i] 
    return render_template('about.html', about_active=True, faq_dictionary = faq_dictionary)

@app.route('/profile')
def prof():

    return render_template('profile.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # You can create a thank_you.html template


@app.route('/oopsNotAvailable')
def oops_page():
    return render_template('oopsNotAvailable.html')


if __name__ == '__main__':
    app.run(debug=True)