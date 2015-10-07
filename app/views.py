from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template("map.html")

@app.route('/readme')
def about():
	return render_template("about.html")