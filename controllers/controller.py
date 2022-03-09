from flask import render_template
from app import app
from models.product_list import orders

@app.route('/')
def index():
    return render_template("index.html", title="Home", orders=orders)
    
@app.route('/orders/<id>')
def order(id):
    coffee = orders[int(id)]
    return render_template("order.html", id=id, title="Ordered items", order=coffee)
    # return "Hello World"