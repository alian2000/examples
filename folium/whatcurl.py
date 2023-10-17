import requests
url ="https://w3schools.com/python/demopage.htm"
print (url)
headers={'x-api-key':'09ba90f6-dcd0-42c0-8c13-5baa6f2377d0'}
print (headers)
resp = requests.get(url,headers=headers)
print (resp.status_code)
print (resp.content)
print(resp.apparent_encoding)
print("----------------------------")
print (resp)
