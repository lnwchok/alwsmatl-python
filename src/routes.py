from src import app
from flask import render_template, request
import src.libs as libs


### First Page
@app.route("/")
def main():
    return render_template('index.html')


### Wall Thickness
@app.route("/wallthk", methods=["POST", "GET"])
def wallcalc():
    if request.method == 'POST':
        material = request.form['material']
        d_p = request.form['d_p']
        d_t = request.form['d_t']
        nps = request.form['nps']


        return request.form['material']
    else:
        return render_template('wall.html', materials=libs.List_input_material())