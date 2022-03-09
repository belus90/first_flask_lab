from flask import render_template
from app import app
from models.product_list import orders

@app.route('/')
def index():
    return render_template("index.html", title="Home", orders=orders)
    