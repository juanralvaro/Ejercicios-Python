from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"