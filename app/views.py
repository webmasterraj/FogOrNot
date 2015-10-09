from flask import render_template
from app import app, jsonFile
import json

@app.route('/')
def index():
	sf_forecasts = jsonFile.query.filter_by(name='sf_forecasts').order_by(jsonFile.created_date.desc()).first().json
	return render_template("map.html",
		jsonfile=json.dumps(sf_forecasts)
	)

@app.route('/readme')
def about():
	return render_template("about.html")