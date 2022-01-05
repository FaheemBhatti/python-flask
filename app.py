
from flask import  Flask , redirect, url_for
from flask.templating import render_template
import requests
import os

# import the MongoClient class
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['TODO_DB_1_PORT_27017_TCP_ADDR'] , 
    27017)
db = client.tododb

@app.route("/")
def todo():
    _items = db.tododb.find()

    items = [item for item in _items]
    return render_template('todo.html' , items=items)

@app.route('/new' , methods=['POST'])
def new():
    item_doc = {
        'name': requests.form['name'],
        'description': requests.form['description']
    }
    db.todo.insert_one(item_doc)
    return redirect(url_for('todo'))


if __name__=="__main__":
    app.run(host='0.0.0.0' , debug=True)
