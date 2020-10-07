from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import the config class
from settings.configs import DevelopmentConfig,ProductionConfig
# import db connection
# from settings.db_connect import conn

app = Flask(__name__)
# tell flask which config settings to use
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from models.inventory import InventoryModel
from models.sales import SalesModel
from models.stock import StockModel

@app.before_first_request
def create_tables():
    db.create_all()
   

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

    inventories = InventoryModel.fetch_all()
    print(inventories) 

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['bp']
        sp = request.form['sp']

        # insert record into the databases
        # cur.execute('INSERT INTO inventories (name, type, bp, sp) VALUES (%s,%s,%s,%s)', (name,type,buying_price,sp))
        # conn.commit()
        
        record = InventoryModel(name=name,type=type, bp=buying_price, sp=sp)
        db.session.add(record)
        db.session.commit()

        print("record has successfully been created")
        return redirect(url_for('inventories'))

    return render_template('inventories.html', all_inventories=inventories)
    
@app.route('/add_stock/<inv_id>', methods=['POST', 'GET'])
def add_stock(inv_id):

    if request.method == 'POST':
        quantity = request.form['quantity']

        new_stock = StockModel(inv_id=inv_id, quantity=quantity)
        db.session.add(new_stock)
        db.session.commit()

        print("Stock added to inventory")
        return redirect(url_for('inventories'))

@app.route('/delete/<inv_id>')
def delete_inventory(inv_id):
    
    record = InventoryModel.query.filter_by(id=inv_id).first()

    if record:

        print("Are you want to delete the record?")

        db.session.delete(record)
        db.session.commit()
        print("Inventory deleted")
    
    else:

        print("Error!! Operation usuccessfull")

    return redirect(url_for('inventories'))
    

@app.route('/charts')
def charts():
    return render_template('charts.html')



