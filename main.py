from flask import Flask, render_template, request

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

@app.route('/inventories', methods=['GET', 'POST'])
def inventories():

    # Open a cursor to perform database operations
    cur = conn.cursor()


    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['bp']
        sp = request.form['sp']

        cur.execute('INSERT INTO inventories (name, type, bp, sp) VALUES (%s,%s,%s,%s)', (name,type,buying_price,sp))
        conn.commit()


    return render_template('inventories.html')
    
@app.route('/charts')
def charts():
    return render_template('charts.html')


