from flask import Flask, render_template, request, redirect
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.get("/")
def index():
	return render_template("index.html")

def ValuePred(to_list_pred):
    to_list = np.array(to_list_pred).reshape(1,64)
    load_model = pickle.load(open("ml_appp.pkl", "rb"))
    result = load_model.predict(to_list)
    return result[0]


@app.post("/result")
def result():
    if request.method == 'POST':
        to_list_pred = request.form.to_dict()
        to_list_pred = list(to_list_pred.values())
        to_list_pred = list(map(float, to_list_pred))
        result = ValuePred(to_list_pred)
        if result == 'Fully Paid':
            prediction = 'Accept his loan'
        else:
            prediction = 'Reject his loan, we think he will charge off'

    #dat = request.form[]
        # put user input values inside a list in order (loan_amount, annual_inc, verification_status, purpose, term, emp_length, application_type)
    #data_list = []
    #for key, val in dat.items():
        #data_list.append(val)
    #vect = log_model(data_list)
    #my_prediction = log_model.predict(data_list)
        # TO BE CHANGED
        # predcition should be either 1 or 2
        #prediction = 0
    return render_template("result.html", prediction =prediction)

if __name__ == "__main__":
    app.run(debug = True, port = 9000)