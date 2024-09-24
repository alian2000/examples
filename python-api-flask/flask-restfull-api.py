import flask
from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)
@app.route('/')
def say_hannah():
    query= flask.Request.args={"a":"1"}
    return "Greet from Hannah from Server"
@app.route("/get_emp_info", methods = ['POST'])
def get_employee_record():
    input_data = json.loads(request.get_json())
    ids = input_data['emp_ids']
    status = input_data['status']
    emp_info = pd.read_csv('emp_info.csv')
    emp_status = pd.read_csv('emp_status.csv')
    emp_status = emp_status[(emp_status['emp_no'].isin(ids)) & (emp_status['status'].isin(status))]
    emp_info = emp_info[emp_info['emp_no'].isin(emp_status['emp_no'])]
    emp_info = pd.merge(emp_info,emp_status,on='emp_no',how='left')
    out_data = emp_info.to_dict(orient='records')
    return jsonify(out_data)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=6123)