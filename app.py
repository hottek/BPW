from flask import Flask, send_from_directory, request

app = Flask(__name__)

fDir = './static/'


@app.route('/')
def index():
    return send_from_directory(fDir, 'index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return 'Bluescreen counter +1'


@app.route('/bpw', methods=['GET'])
def bpw():
    return 'one'


if __name__ == '__main__':
    app.run(port=8000)
