from flask import Flask, flash, redirect, render_template, request, session, abort
import mysql.connector
import json

app = Flask(__name__)

@app.route("/")
def index():
# connect to the database
    mydb = mysql.connector.connect(
        host="dbbikes.cydtuzfevnm7.us-east-1.rds.amazonaws.com",
        user="root",
        passwd="whiterabbit",
        database="dbbikes"
    )
# prebuilt function in mysql to interaction with a database
    mycursor = mydb.cursor(dictionary=True)
# Next, we setup our SQL query
    mycursor.execute("SELECT name, latitude, longitude FROM stations")
# Then we get some stuff back... By appending a variable to the response of the query
    myresult = mycursor.fetchall()
# We make an empty list
    station_list=[]
# for every result we get back, we add that to the list in a new index
    for x in myresult:
        station_list.append(dict((x)))
# This 'welcomemessage' is an example of passing a variable back into the front end using jinjas2
    welcomemessage = "Hello"
# Then we ALWAYS PRINT STUFF TO MAKE SURE IT'S ACTUALLY RIGHT'
    print(station_list)
# Then we return something... This could be a html page, or variables... It's usually both though

# this json dumps function is essential in returning data back to the front end correctly

    station_list = json.dumps(station_list)

    return render_template("/index.html", welcomemessage=welcomemessage, station_list=station_list)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)