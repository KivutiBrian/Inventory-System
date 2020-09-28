from flask import Flask, render_template

# import db connection
from settings.db_connect import conn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('contact.html')

@app.route('/contact-us')
def contact():
    return render_template('about.html')

@app.route('/inventories')
def inventories():
    return render_template('inventories.html')
    
@app.route('/charts')
def charts():
    return render_template('charts.html')


