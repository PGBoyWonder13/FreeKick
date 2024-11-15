from flask import Flask, redirect, render_template, request, url_for
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


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

    def __repr__(self):
        return f'<Contact {self.name}>'

@app.route('/')
def index():

    return render_template('index.html', home_active=True)


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form.get('name')
        email = request.form.get('email')
        comments = request.form.get('comments')

        # Create a new Contact instance and add it to the database
        new_contact = Contact(name=name, email=email, comments=comments)

        # Add the new contact to the session and commit
        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('contact.html', contact_active=True)

@app.route('/about')
def info():
    faq_listofQuestions = ["What is FreeKick?", "What FreeKick offers?", "Is it true that I can stay up to date with the latest AI, tech, and soccer analytics?", \
        "Who runs FreeKick?","Is FreeKick a for or not-for profit organization?"]
    faq_listofAnswers = ["FreeKick LLC is a company that connects communites to the most immersive US 2026 World Soccer Analytics and AI experience. "  \
        ,"FreeKick provides provides services that engage the community with the biggest sporting event in the World the 2026 Soccer World Cup.", "Yes FreeKick takes advantage of AI, soccer analytics, passionate 2026 World Cup enthusiasts to keep you updated." \
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

if __name__ == '__main__':
    app.run(debug=True)