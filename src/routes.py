from src import app
from flask import render_template, jsonify
import src.db as db


### First Page
@app.route("/")
def main():
    return render_template('index.html')


### Wall Thickness
@app.route("/wallthk")
def wallcalc():
    return render_template('wall.html')