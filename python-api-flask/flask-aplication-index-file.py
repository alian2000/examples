import time

from flask import Flask,render_template, flash, redirect
from flask_restful import Resource, Api, reqparse

#https://www.blog.duomly.com/python-api-tutorial/

# i named it application and not app to show this is just any name
#__name_ is just the name of the python script
"""Probably the most interesting way to load configurations is from an
    environment variable pointing to a file::
 app.config.from_envvar('YOURAPPLICATION_SETTINGS from environment variable on a POD')
 class Config(dict):
 
 """
b='dir'
print(exec (b))
application = Flask(__name__)
api = Api(application)
print (application)
print("-------------------------------------")
STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}


# creating a class with the name Student
# __init__ to initialize only and not to set new values
# create a setter method to set new values

class student:
    def __init__(self, name, age):
        self.name = name  # object_variables or property = parameter
        self.age = age  # object_variables or property = parameter

    def get_name(self):
        return self.name
        # You can use the return statement to make your functions send Python objects back
        # to the caller code. These objects are known as the function’s return value.
        # You can use them to perform further computation in your programs.

    def get_age(self):
        return self.age

    def get_student(self):
        return self.name, self.age

    def set_student(self, name, age):
        self.name = name
        self.age = age


student1 = student("usama", 48)  # create an object or instance of the class

# setting the age using setter
student1.set_student("tamer", 15)

# retrieving age using getter
print(student1.get_name())
print("-----------------------------------")
print(student1.get_student())
print("************************************")

print(student1.name)
print(student1.age)

student1.set_student("wafa", 41)
print("--------------------------------------")
print(student1.name)
print(student1.age)
parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return STUDENTS




    def post(self):
        parser.add_argument("name", location="args")
        parser.add_argument("age", location="args")
        parser.add_argument("spec", location="args")
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
        }
        return STUDENTS[student_id], 201
class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]

    def put(self, student_id):
        parser.add_argument("name", location="args")
        parser.add_argument("age", location="args")
        parser.add_argument("spec", location="args")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args["name"] is not None else student["name"]
            student["age"] = args["age"] if args["age"] is not None else student["age"]
            student["spec"] = args["spec"] if args["spec"] is not None else student["spec"]
            return student, 200

    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
            return '', 204

@application.route('/')
def hello_world():
    print("Alive")
    return render_template('index.html')

api.add_resource(Student, '/students/<student_id>')

api.add_resource(StudentsList, '/students/')
@application.route('/sts')
def say_hannah():
    return "Greet from Hannah from Server"
@application.route('/friday')
def say_friday():
    return


if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0',port=5000)