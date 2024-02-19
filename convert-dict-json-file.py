"""
JSON is a data exchange format used all over the internet. JSON (JavaScript Object Notation) can be used by all high level programming languages.
There are four different methods in the python json module to work with python objects and JSON altogether. Those four are mentioned as below:
json.dumps() - This method allows you to convert a python object into a serialized JSON object.
json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)
json.loads() - Deserializes a JSON object to a standard python object.
json.load() - Deserializes a JSON file object into a standard python object.

"""

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x["cars"][1]["mpg"])
print(type(x))
print("------------------------------------------")
json_object=json.dumps(x)
print(type(json_object))

print(json_object)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print("------------------------------------------")

print("------------------------------------------")
print ((x['age']),(x['name']))
print (x['name'])
print (json_object)
#print (json.dumps(x, indent=4))
#y= json.loads(x)
#print (y["age"])


