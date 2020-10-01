from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import the config class
from settings.configs import DevelopmentConfig,ProductionConfig
# import db connection
from settings.db_connect import conn

app = Flask(__name__)
# tell flask which config settings to use
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

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
    # get all inventories
    cur.execute('SELECT * FROM inventories')
    records = cur.fetchall()
    print(records)    

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['bp']
        sp = request.form['sp']

        # insert record into the database
        cur.execute('INSERT INTO inventories (name, type, bp, sp) VALUES (%s,%s,%s,%s)', (name,type,buying_price,sp))
        conn.commit()

        print("record has successfully been created")
        return redirect(url_for('inventories'))

    return render_template('inventories.html', all_inventories=records)
    
@app.route('/charts')
def charts():
    return render_template('charts.html')


