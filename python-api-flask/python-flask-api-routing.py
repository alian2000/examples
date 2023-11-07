from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
parser = reqparse.RequestParser()

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}



@app.route("/")
def hello_world():
    print("Alive")
    return "Hello, World!"

@app.route('/greet')
def say_hannah():
    return "Greet from Hannah from Server"

@app.route('/aqsa')
def say_aqsa():
    return 'May Allah accept your prayers'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
    return 'Hello Mr. Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
     #returns the post, the post_id should be an int
     return str(post_id)
if __name__ == "__main__":
    app.run(debug=True)
