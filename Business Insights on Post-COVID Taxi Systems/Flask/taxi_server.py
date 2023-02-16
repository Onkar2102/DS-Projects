from pandas import core


from flask import Flask
import pickle

file = open('')


# create new server with name same as module name
app = Flask(__name__)
print(__name__)
print(app)


# start the server

@app.route("/", methods=["GET"])
def root():
    return "Flask page...................."


# predicting salary
@app.route("/predict", methods=["GET"])
def predict_salary():
    return "predicting salary"


app.run(debug=True)
