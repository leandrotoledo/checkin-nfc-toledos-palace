#!/usr/bin/env python
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       with open('../data/tags.csv', 'rb') as file:
          reader = csv.reader(file)
          tags = [row for row in reader]

       return render_template('index.html', tags=tags)
    if request.method == 'POST':
       new = []
       with open('../data/tags.csv', 'rb') as file:
          reader = csv.reader(file)
          for row in reader:
             if row[0] == request.form['id-nfc']:
                try:
                   row[1] = request.form['name-nfc']
                except IndexError:
                   row.append(request.form['name-nfc'])

             new.append(row)

       print new
   
       with open('../data/tags.csv', 'wb') as file:
          for row in new:
             if len(row) == 2:
                file.write('%s,%s\n' % (row[0], row[1]))
             else:
                file.write('%s\n' % (row[0],))


       with open('../data/tags.csv', 'rb') as file:
          reader = csv.reader(file)
          tags = [row for row in reader]

       return render_template('index.html', tags=tags)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
