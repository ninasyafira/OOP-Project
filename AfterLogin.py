from flask import Flask, render_template, request
from wtforms import Form, StringField, validators



app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/hey')
def hey():
    return render_template('homepage2.html')


@app.route('/nov')
def nov():
    return render_template('nov.html')

@app.route('/dec2016')
def dec2016():
    return render_template('dec2016.html')

@app.route('/nov2016')
def nov2016():
    return render_template('nov2016.html')

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/graph')
def graph():
    return render_template('Graph.html')

@app.route('/details')
def details():
    return render_template('Details.html')

if __name__ == '__main__':
    app.run()
