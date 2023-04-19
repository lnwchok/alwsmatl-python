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
        d_p = float(request.form['d_p'])
        d_t = float(request.form['d_t'])
        nps = request.form['nps']
        
        # Define Stress
        stress = libs.findAllowStress(material,d_t)
        # Define E, W, Y-factor
        Ef = 0
        Wf = 0
        Yf = 0

        return "Stress = {:.2f}".format(stress)
    else:
        return render_template('wall.html', materials=libs.List_input_material(), pipesize=libs.List_input_NPS())