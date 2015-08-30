#!/usr/bin/env python
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'GET':
       with open('../data/tags.csv', 'rb') as file:
          reader = csv.reader(file)
          tags = [row for row in reader]

       return render_template('index.html', tags=tags)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
