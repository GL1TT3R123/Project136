import pandas
from data import data
from flask import Flask,jsonify,request

app= Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success",
    }),200

@app.route("/stars")
def stars():
    star= request.args.get("name")
    planet_data= next(item for item in data if item["name"]==star)
    return jsonify({
        "data":planet_data,
        "message":"success"
    }),200
app.run()