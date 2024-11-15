from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
faq_dictionary = {}

@app.route('/')
def index():

    return render_template('index.html', home_active=True)


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/contact')
def contact():
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