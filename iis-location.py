import json
import time

import requests

url ="http://api.open-notify.org/iss-now.json"
#print (url)
headers={'x-api-key':'09ba90f6-dcd0-42c0-8c13-5baa6f2377d0'}
#print (headers)
for i in range (0,10):
    resp = requests.get(url,headers=headers)
    #print (resp.status_code)
    ##print ("------------------------------------")
    #print (resp.content)
    #print ("------------------------------------")

    iprequest=resp.text
    dict=json.loads(iprequest)
    #print(f"Response: {r.json()}")
    #print (type(dict))
    #print(dict)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print ("location-of-iss =",dict["iss_position"])

    print ("longitude-of-iss =",dict["iss_position"]["longitude"])
    print ("latitude-of-iss =",dict["iss_position"]["latitude"])
    time.sleep(10)

#print ("***********************************")
