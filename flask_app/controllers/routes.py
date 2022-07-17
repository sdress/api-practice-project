from flask_app import app
from flask import render_template, jsonify 
from flask_app.models.model_name import Class_Name
import os
import requests

# bcrypt = Bcrypt(app)

@app.route('/searching')
def get_api():
    r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=GUbcVwow399v0AHvkHKPk9WcM9HMuJXI3Pp5gO9')
    return jsonify( r.json() )

@app.route('/')
def show_dashboard():
    return 'This is the Dashboard'
