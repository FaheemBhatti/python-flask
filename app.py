from flask import  Flask , redirect, url_for, jsonify
from flask.templating import render_template
from pymongo import MongoClient
import json




app = Flask(__name__)
myclient=MongoClient('db',27017)

db = myclient["testdb"]
mycol = db["table"]


@app.route("/")
def todo():
    return 'Hello World'

@app.route('/new' , methods=['POST'])
def new():
    mylist = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)
    return jsonify("Done One"), 200

@app.route('/get' , methods=['GET'])
def get():
    getting_one = db.table.find()
    return json.dumps(getting_one, default=str)
  

if __name__=="__main__":
     app.run(host='0.0.0.0' , debug=True)