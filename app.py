from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move_button', methods=['POST'])
def move_button():
    x = random.randint(0, int(request.form['width']) - 100)
    y = random.randint(0, int(request.form['height']) - 50)
    return {'x': x, 'y': y}

@app.route('/accepted', methods=['POST'])
def accepted():
    return 'Eu te amo meu amor, lanchinho mais tarde?'

@app.route('/denied', methods=['POST'])
def denied():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)