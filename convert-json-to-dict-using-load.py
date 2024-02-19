"""
JSON is a data exchange format used all over the internet. JSON (JavaScript Object Notation) can be used by all high level programming languages.
There are four different methods in the python json module to work with python objects and JSON altogether. Those four are mentioned as below:
json.dumps() - This method allows you to convert a python object into a serialized JSON object.
json.dump() - This method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)
json.loads() - Deserializes a JSON object to a standard python object.
json.load() - Deserializes a JSON file object into a standard python object.

"""
import json

# read file
with open('sample.json', 'r') as myfile:
    data = json.load(myfile)

# parse file
print(type(data))
#print(data)

obj = data
print(type(obj))
# print(obj)
print(obj["name"])
print(obj["age"])
obj["age"]=150

with open('updatedsample.json', 'w') as newjsonfile:
    json.dump(obj,newjsonfile) 
    
