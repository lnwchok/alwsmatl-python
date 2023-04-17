from src import app
from flask import render_template, jsonify
import src.db as db

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/material")
def material():
    return render_template('index.html', name=db.getname())