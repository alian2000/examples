from urllib import response
import requests
r = requests.get('https://xkcd.com/353/')
image1=requests.get('https://imgs.xkcd.com/comics/python.png')
print (r.text)
#print(image1.content)
with open('comic10.png', 'wb') as f:
    f.write(image1.content)
