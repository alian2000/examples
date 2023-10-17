import json

import requests
url ="http://ip-api.com/json/"
print (url)
headers={'x-api-key':'09ba90f6-dcd0-42c0-8c13-5baa6f2377d0'}
#print (headers)
resp = requests.get(url,headers=headers)
print (resp.status_code)
print ("------------------------------------")
print (resp.content)
print ("------------------------------------")

iprequest=resp.text
dict=json.loads(iprequest)
#print(f"Response: {r.json()}")
print (type(dict))
print(dict)
print ("customer_ip_address =",dict["query"])
print ("***********************************")



print(ip["status"])
print(ip["city"])
print(ip["query"])
print(ip["isp"])


