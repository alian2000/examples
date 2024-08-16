from flask import Flask
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)  # creating the application instance
api = Api(app)  # creating the application instance

@app.route('/')
def say_myName():
    return "Greet from Usama, Hello World from Server"

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0',port=8080)
