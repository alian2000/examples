# command prompt - installing requests package
# Python code to test
import requests,json
# sample request
data = {"emp_ids":["1001","1002","1003"],"status":["active"]}
# Hitting the API with a POST request
ot = requests.post(url='http://192.168.86.34:6123/get_emp_info', json=json.dumps(data))
print(ot.json())
print(ot)
# Response JSON
[{
 'cmp': 'ABC',
 'emp_no': 1001,
 'name': 'Ben',
 'salary': 100000,
 'status': 'active'
}, {
 'cmp': 'MNC',
 'emp_no': 1002,
 'name': 'Jon',
 'salary': 200000,
 'status': 'active'
}]