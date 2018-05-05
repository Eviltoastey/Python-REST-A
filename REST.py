from flask_restful import Resource, Api
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/customer", methods=['GET'])
def customer():
    return jsonify({
        "id" : 1,
        "name" : "customer",
        "email" : "cusstomer@gmail.com"
        })

if __name__ == '__main__':
    app.run(debug = True)

@app.route("/cart", methods=['GET'])
def cart():
    return jsonify({
        "id" : 1,
        "customer_id" : 1
        })

if __name__ == '__main__':
    app.run(debug = True)
