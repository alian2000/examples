from flask import Flask, render_template
import csv

app = Flask(__name__)
#print "---------------------------------------"
@app.route('/csv')
def index():
    data = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if it exists
        for row in csv_reader:
            data.append(row)
            print(row)
    return render_template('index2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8081)