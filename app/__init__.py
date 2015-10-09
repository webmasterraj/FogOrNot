import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class jsonFile(db.Model):
    __tablename__ = "json_files"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    json = db.Column(db.Text())
    created_date = db.Column(db.Date())

    def __init__(self, name, json, created_date):
        self.name = name
        self.json = json
        self.created_date = created_date

    def __repr__(self):
        return '<Name %r>' % self.name

from app import views


