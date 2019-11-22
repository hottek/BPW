from flask import Flask, send_from_directory, request
import sqlite3
import datetime
import jinja2

app = Flask(__name__)

fDir = '/app/static'
db = "/database/database.db"


@app.route('/')
def index():
    print("I should server", flush=True)
    return send_from_directory(fDir, 'index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')

    conn = sqlite3.connect(db)
    c = conn.cursor()

    today = datetime.datetime.now()
    datestring = f'{today.year}-{today.month}-{today.day}'

    c.execute("""INSERT INTO Log (name, date) VALUES (?, ?);""", (str(name), str(datestring)))
    conn.commit()
    conn.close()
    return getRIESENstring('Bluescreen counter +1')


@app.route('/bpw', methods=['GET'])
def bpw():
    conn = sqlite3.connect(db)
    c = conn.cursor()

    d = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().isoweekday() % 7)
    startofweek = f'{d.year}-{d.month}-{d.day}'

    data = c.execute("""SELECT * FROM Log WHERE date(date) > date(?);""", (str(startofweek),)).fetchall()
    conn.commit()
    conn.close()

    return getRIESENstring(len(data))


def getRIESENstring(muchgold):
    template = jinja2.Template("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
        .row {
            margin-top: 50px;
        }
    </style>
</head>
<body class="text-center">
    <div class="row">
        <div class="col-sm-3"></div>
        <div class="col-sm-6">
            {% for attr in attrs %}
      <h1 class="display-1">{{attr}}</h1>
      {% endfor %}
        </div>
        <div class="col-sm-3"></div>
    </div>
</body>
</html>""")
    return template.render({'attrs': [muchgold]})
