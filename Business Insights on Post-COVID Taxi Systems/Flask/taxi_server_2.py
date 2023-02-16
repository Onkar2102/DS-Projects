import pandas as pd
from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

# loading the pickle files

# # linear model pickle file
# file_1 = open("taxi_fare_linear.pkl", 'rb')
# model_linear = pickle.load(file_1)
# file_1.close()

# Random forest model
## total amount
file_1 = open("taxi_fare_RANDOM1.pkl", 'rb')
model_random_total = pickle.load(file_1)
file_1.close()

## fare amount
file_2 = open("taxi_fare_RANDOM2.pkl", 'rb')
model_random_fare = pickle.load(file_2)
file_2.close()

## tip amount
file_3 = open("taxi_fare_RANDOM3.pkl", 'rb')
model_random_tip = pickle.load(file_3)
file_3.close()

# # XG_Boost algorithm
# file_3 = open("taxi_fare_XG.pkl", 'rb')
# model_xg = pickle.load(file_3)
# file_3.close()

# creating flask app with same name as module name
app = Flask(__name__, static_url_path='/static')

# importing csv file containing values of dropdown
df = pd.read_csv("New_taxi_zones_2.csv")

# creating list to store values of csv file
list = df['zone']

# declaring variables
dp1 = 0
dp2 = 0
dist = 0
vendor = [1.0, 2.0]
vendor_name = 0

# importing csv file for finding distance
df_2 = pd.read_csv('fin_distance.csv')


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html", len=len(list), options=list,vendor_list=vendor,vendor_len=len(vendor))


#
@app.route("/set", methods=["POST"])
def set():
    global dp1, dp2, dist, vendor
    dp1 = request.form.get("dropdown_1")
    dp2 = request.form.get("dropdown_2")

    print(dp1, type(dp1))
    print(dp2, type(dp2))

    vendor_name = request.form.get("dropdown_3")

    for i in range(0, len(df_2['trip_distance'])):
        if df_2['pickup'][i] == dp1 and df_2['dropoff'][i] == dp2:
            dist = float(df_2['trip_distance'][i])
            break
    print(dist, type(dist))
    total = model_random_total.predict([[vendor_name, float(dist)]])
    print(total, type(total))

    fare = model_random_fare.predict([[vendor_name, float(dist)]])
    print(fare, type(fare))

    tip = model_random_tip.predict([[vendor_name, float(dist)]])
    print(tip, type(tip))

    total1 = float("{:.2f}".format(total[0]))
    print(total1)
    # return render_template("cost.html", total1=total1)

    fare1 = float("{:.2f}".format(fare[0]))
    print(fare1)
    # return render_template("cost.html", fare1=fare1)

    tip1 = float("{:.2f}".format(tip[0]))
    print(tip1)
    return render_template("cost.html",total1=total1, fare1=fare1, tip1=tip1)


@app.route("/powerbi", methods=["POST"])
def power_bi():
    return render_template("pbi.html")


# post route for linear model
# @app.route("/linear", methods=["POST"])
# def linear():
#     fare = model_linear.predict([[dist]])
#     return f"<h1>Fare is :  = {fare[0][0]} $</h1>"


# post route for random forest algorithm
# @app.route("/cost", methods=["POST"])
# def cost():


#
# @app.route("/xg", methods=["POST"])
# def xg():
#     fare = model_xg.predict(float(dist))
#     return f"<h1>Fare is :  = {fare} $</h1>"


app.run(debug=True)




# import pandas as pd
# from flask import Flask, render_template, request, redirect
# import pickle
# import numpy as np
#
# # loading the pickle files
#
# # linear model pickle file
# file_1 = open("taxi_fare_linear.pkl", 'rb')
# model_linear = pickle.load(file_1)
# file_1.close()
#
# # Random forest model
# file_2 = open("taxi_fare_RANDOM.pkl", 'rb')
# model_random = pickle.load(file_2)
# file_2.close()
#
# # XG_Boost algorithm
# file_3 = open("taxi_fare_XG.pkl", 'rb')
# model_xg = pickle.load(file_3)
# file_3.close()
#
# # creating flask app with same name as module name
# app = Flask(__name__, static_url_path='/static')
#
# # importing csv file containing values of dropdown
# df = pd.read_csv("New_taxi_zones_2.csv")
#
# # creating list to store values of csv file
# list = df['zone']
#
# # declaring variables
# dp1 = 0
# dp2 = 0
# dist = 0
#
# # importing csv file for finding distance
# df_2 = pd.read_csv('fin_distance.csv')
#
#
# @app.route("/", methods=["GET"])
# def root():
#     return render_template("index.html", len=len(list), options=list)
#
#
# #
# @app.route("/set", methods=["POST"])
# def set():
#     global dp1, dp2, dist
#     dp1 = request.form.get("dropdown_1")
#     dp2 = request.form.get("dropdown_2")
#     print(dp1, type(dp1))
#     print(dp2, type(dp2))
#     for i in range(0, len(df_2['trip_distance'])):
#         if df_2['pickup'][i] == dp1 and df_2['dropoff'][i] == dp2:
#             dist = float(df_2['trip_distance'][i])
#             break
#     print(dist, type(dist))
#     fare = model_random.predict([[float(dist)]])
#     # fare=10
#     print(fare, type(fare))
#
#     cost = float("{:.2f}".format(fare[0]))
#     print(cost)
#     return render_template("cost.html",cost=cost)
#
#
# @app.route("/powerbi", methods=["POST"])
# def power_bi():
#     return render_template("pbi.html")
#
#
# # post route for linear model
# # @app.route("/linear", methods=["POST"])
# # def linear():
# #     fare = model_linear.predict([[dist]])
# #     return f"<h1>Fare is :  = {fare[0][0]} $</h1>"
#
#
# # post route for random forest algorithm
# # @app.route("/cost", methods=["POST"])
# # def cost():
#
#
# #
# # @app.route("/xg", methods=["POST"])
# # def xg():
# #     fare = model_xg.predict(float(dist))
# #     return f"<h1>Fare is :  = {fare} $</h1>"
#
#
# app.run(debug=True)
