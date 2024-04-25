import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://raw.githubusercontent.com/alian2000/examples/main/sample.json')

#print the response text (the content of the requested file):
print(x.text)
print(type(x.text))
