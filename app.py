from flask import Flask, flash, redirect, url_for, render_template, request, session, abort, jsonify
import mysql.connector
import json
import datetime
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
from datetime import date
import holidays

app = Flask(__name__)

@app.route("/graphs", methods=['POST'])
def graphs():
    # DATABASE CONNECTION
    mydb = mysql.connector.connect(
        host="dbbikes.cydtuzfevnm7.us-east-1.rds.amazonaws.com",
        user="root",
        passwd="whiterabbit",
        database="dbbikes"
    )
    # print("TESSSDFNISDKFSLDIFN")
    radio = request.form.get('radio')
    stn = request.form.get('id')


    # GENERATE STATION LIST
    # prebuilt function in mysql to interact with a database
    mycursor = mydb.cursor(dictionary=True)
    # Next, we setup our SQL query
    mycursor.execute("SELECT * from stations a, temp_table b where a.number= b.number order by a.address")
    # Then we get some stuff back... By appending a variable to the response of the query
    myresult = mycursor.fetchall()
    # We make an empty list
    station_list = []
    # for every result we get back, we add that to the list in a new index

    for x in myresult:
        station_list.append(dict((x)))
    # This 'welcomemessage' is an example of passing a variable back into the front end using jinjas2
    welcomemessage = "Hello, welcome to Dublin Bikes!"
    # Then we ALWAYS PRINT STUFF TO MAKE SURE IT'S ACTUALLY RIGHT'
    print(station_list)

    # this json dumps function is essential in returning data back to the front end correctly
    station_list = json.dumps(station_list)



    x = datetime.datetime.now()
    station_number = stn
    dayx = x.strftime("%A")
    hourx = int(x.strftime("%H"))
    print(dayx)
    print(hourx)
    print("this is radio:", radio)
    print("this is stn:", stn)

    # CHART: AVG BIKES BY DAY/HOUR

    if radio == "available_bikes":
        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now = []
        for i in myresult:
            print(i)
            now.append(i)
        nowx = int((now[0][0]))
        print("Now:", nowx)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 1,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now1 = []
        for i in myresult:
            print(i)
            now1.append(i)
        now1x = int((now1[0][0]))
        print("1hr:", now1x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, (hourx + 2),))
        myresult = mycursor.fetchall()
        # print(myresult)
        now2 = []
        for i in myresult:
            print(i)
            now2.append(i)
        now2x = int((now2[0][0]))
        print("2hr:", now2x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 3,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now3 = []
        for i in myresult:
            print(i)
            now3.append(i)
        now3x = int((now3[0][0]))
        print("3hr:", now3x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 4,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now4 = []
        for i in myresult:
            print(i)
            now4.append(i)
        now4x = int((now4[0][0]))
        print("4hr:", now4x)

        times = ["Now", "1hr", "2hr", "3hr", "4hr"]
        qty = [nowx, now1x, now2x, now3x, now4x]

        # CHART: AVG STATION OCCUPANCY

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 1)  AND number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        mon = []
        for i in myresult:
            # print(i)
            mon.append(i)
        monday = int((mon[0][0]))
        print("Monday:", monday)

        mycursor.execute(
            "SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 2)  AND number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        tue = []
        for i in myresult:
            # print(i)
            tue.append(i)
        tuesday = int((tue[0][0]))
        print("Tuesday:", tuesday)

        mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 3) and number = %s",
                         (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        wed = []
        for i in myresult:
            # print(i)
            wed.append(i)
        wednesday = int((wed[0][0]))
        print("Wednesday:", wednesday)

        mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 4) and number = %s",
                         (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        thur = []
        for i in myresult:
            # print(i)
            thur.append(i)
        thursday = int((thur[0][0]))
        print("Thursday:", thursday)

        mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 5) and number = %s",
                         (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        fri = []
        for i in myresult:
            # print(i)
            fri.append(i)
        friday = int((fri[0][0]))
        print("Friday:", friday)

        mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 6) and number = %s",
                         (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        sat = []
        for i in myresult:
            # print(i)
            sat.append(i)
        saturday = int((sat[0][0]))
        print("Saturday:", saturday)

        mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 7) and number = %s",
                         (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        sun = []
        for i in myresult:
            # print(i)
            sun.append(i)
        sunday = int((sun[0][0]))
        print("Sunday:", sunday)

        labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_values = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    else:
        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now = []
        for i in myresult:
            print(i)
            now.append(i)
        nowx = int((now[0][0]))
        print("Now:", nowx)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 1,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now1 = []
        for i in myresult:
            print(i)
            now1.append(i)
        now1x = int((now1[0][0]))
        print("1hr:", now1x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, (hourx + 2),))
        myresult = mycursor.fetchall()
        # print(myresult)
        now2 = []
        for i in myresult:
            print(i)
            now2.append(i)
        now2x = int((now2[0][0]))
        print("2hr:", now2x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 3,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now3 = []
        for i in myresult:
            print(i)
            now3.append(i)
        now3x = int((now3[0][0]))
        print("3hr:", now3x)

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",
            (station_number, dayx, hourx + 4,))
        myresult = mycursor.fetchall()
        # print(myresult)
        now4 = []
        for i in myresult:
            print(i)
            now4.append(i)
        now4x = int((now4[0][0]))
        print("4hr:", now4x)

        times = ["Now", "1hr", "2hr", "3hr", "4hr"]
        qty = [nowx, now1x, now2x, now3x, now4x]

        # CHART: AVG STATION OCCUPANCY

        mycursor = mydb.cursor(dictionary=False)
        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 1)  AND number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        mon = []
        for i in myresult:
            # print(i)
            mon.append(i)
        monday = int((mon[0][0]))
        print("Monday:", monday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 2)  AND number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        tue = []
        for i in myresult:
            # print(i)
            tue.append(i)
        tuesday = int((tue[0][0]))
        print("Tuesday:", tuesday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 3) and number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        wed = []
        for i in myresult:
            # print(i)
            wed.append(i)
        wednesday = int((wed[0][0]))
        print("Wednesday:", wednesday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 4) and number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        thur = []
        for i in myresult:
            # print(i)
            thur.append(i)
        thursday = int((thur[0][0]))
        print("Thursday:", thursday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 5) and number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        fri = []
        for i in myresult:
            # print(i)
            fri.append(i)
        friday = int((fri[0][0]))
        print("Friday:", friday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 6) and number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        sat = []
        for i in myresult:
            # print(i)
            sat.append(i)
        saturday = int((sat[0][0]))
        print("Saturday:", saturday)

        mycursor.execute(
            "SELECT avg(available_bike_stands) from availability where (DAYOFWEEK(last_update) = 7) and number = %s",
            (station_number,))
        myresult = mycursor.fetchall()
        # print(myresult)
        sun = []
        for i in myresult:
            # print(i)
            sun.append(i)
        sunday = int((sun[0][0]))
        print("Sunday:", sunday)

        labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_values = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

    # RETURN TO FRONT END
    # Then we return something... This could be a html page, or variables... It's usually both though
    return render_template ("/index.html",welcomemessage=welcomemessage, station_list=station_list,
                            labels=labels,day_values=day_values, times=times, qty=qty)

@app.route("/", methods=['GET','POST'])
def index():
    radio = request.form.get('radio')
    #stn = request.form.get('id')


# DATABASE CONNECTION
    mydb = mysql.connector.connect(
        host="dbbikes.cydtuzfevnm7.us-east-1.rds.amazonaws.com",
        user="root",
        passwd="whiterabbit",
        database="dbbikes"
    )
# GENERATE STATION LIST
    # prebuilt function in mysql to interact with a database
    mycursor = mydb.cursor(dictionary=True)
    # Next, we setup our SQL query
    mycursor.execute("SELECT * from stations a, temp_table b where a.number= b.number order by a.address")
    # Then we get some stuff back... By appending a variable to the response of the query
    myresult = mycursor.fetchall()
    # We make an empty list
    station_list=[]
    # for every result we get back, we add that to the list in a new index

    for x in myresult:
        station_list.append(dict((x)))
    # This 'welcomemessage' is an example of passing a variable back into the front end using jinjas2
    welcomemessage = "Hello, welcome to Dublin Bikes!"
    # Then we ALWAYS PRINT STUFF TO MAKE SURE IT'S ACTUALLY RIGHT'
    print(station_list)

    # this json dumps function is essential in returning data back to the front end correctly
    station_list = json.dumps(station_list)

# GENERATE CHARTS
    # input variables
    x = datetime.datetime.now()
    station_number = 99
    dayx = x.strftime("%A")
    hourx = int(x.strftime("%H"))
    print(dayx)
    print(hourx)
    print("this is radio:", radio)
    # print("this is stn:", stn)


# # CHART: AVG BIKES BY DAY/HOUR
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",( station_number, dayx, hourx,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     now=[]
#     for i in myresult:
#         print(i)
#         now.append(i)
#     nowx = int((now[0][0]))
#     print("Now:", nowx)
#
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",( station_number, dayx, hourx+1,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     now1 = []
#     for i in myresult:
#         print(i)
#         now1.append(i)
#     now1x = int((now1[0][0]))
#     print("1hr:", now1x)
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",( station_number, dayx, (hourx+2),))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     now2 = []
#     for i in myresult:
#         print(i)
#         now2.append(i)
#     now2x = int((now2[0][0]))
#     print("2hr:", now2x)
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",( station_number, dayx, hourx+3,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     now3 = []
#     for i in myresult:
#         print(i)
#         now3.append(i)
#     now3x = int((now3[0][0]))
#     print("3hr:", now3x)
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where number = %s and (DAYNAME(last_update) = %s) AND (HOUR(last_update) = %s)",( station_number, dayx, hourx+4,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     now4 = []
#     for i in myresult:
#         print(i)
#         now4.append(i)
#     now4x = int((now4[0][0]))
#     print("4hr:", now4x)
#
#
#     times = ["Now", "1hr", "2hr", "3hr", "4hr"]
#     qty = [nowx, now1x, now2x, now3x, now4x]
#
# # CHART: AVG STATION OCCUPANCY
#
#     mycursor = mydb.cursor(dictionary=False)
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 1)  AND number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     mon = []
#     for i in myresult:
#         # print(i)
#         mon.append(i)
#     monday = int((mon[0][0]))
#     print("Monday:", monday)
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 2)  AND number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     tue = []
#     for i in myresult:
#         # print(i)
#         tue.append(i)
#     tuesday = int((tue[0][0]))
#     print("Tuesday:", tuesday)
#
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 3) and number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     wed = []
#     for i in myresult:
#         # print(i)
#         wed.append(i)
#     wednesday = int((wed[0][0]))
#     print("Wednesday:", wednesday)
#
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 4) and number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     thur = []
#     for i in myresult:
#         # print(i)
#         thur.append(i)
#     thursday = int((thur[0][0]))
#     print("Thursday:", thursday)
#
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 5) and number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     fri = []
#     for i in myresult:
#         # print(i)
#         fri.append(i)
#     friday = int((fri[0][0]))
#     print("Friday:", friday)
#
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 6) and number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     sat = []
#     for i in myresult:
#         # print(i)
#         sat.append(i)
#     saturday = int((sat[0][0]))
#     print("Saturday:", saturday)
#
#
#     mycursor.execute("SELECT avg(available_bikes) from availability where (DAYOFWEEK(last_update) = 7) and number = %s",(station_number,))
#     myresult = mycursor.fetchall()
#     # print(myresult)
#     sun = []
#     for i in myresult:
#         # print(i)
#         sun.append(i)
#     sunday = int((sun[0][0]))
#     print("Sunday:", sunday)
#
#     labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     day_values = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]


# -------------------------------------------------------------------------------
# PREDICTIVE MODEL

# this would import the model... we don't want our front end to look really messy so its not going in. this is how we would send it to the front end if we were
# with open('model.pkl', 'rb') as handle:
#     model = pickle.load(handle)
# @app.route("/predict")
# def predict(X_test):
#     # now we can call various methods over model as as:
#     # Let X_test be the feature for which we want to predict the output
#     result = model.predict(X_test)
#     return jsonify(result) 
# -------------------------------------------------------------------------------


# RETURN TO FRONT END
    # Then we return something... This could be a html page, or variables... It's usually both though
    return render_template("/index.html", welcomemessage=welcomemessage, station_list=station_list)
                           #labels=labels, day_values=day_values, times=times, qty=qty)

ie_holidays = holidays.IE()
print("holidays", date(2017,12,25) in ie_holidays)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)