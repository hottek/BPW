from flask import Flask, send_from_directory, request
import sqlite3, datetime, config

app = Flask(__name__)

fDir = './static/'
db = config.dbPath() # Path to db


@app.route('/')
def index():
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
    return 'Bluescreen counter +1'


@app.route('/bpw', methods=['GET'])
def bpw():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    d = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().isoweekday() % 7)
    startofweek = f'{d.year}-{d.month}-{d.day}'
    data = c.execute("""SELECT * FROM Log WHERE date(date) > date(?);""", (str(startofweek),)).fetchall()
    conn.commit()
    print(len(data))
    print(data[0])
    conn.close()

    return str(len(data))


if __name__ == '__main__':
    app.run(port=8000)
