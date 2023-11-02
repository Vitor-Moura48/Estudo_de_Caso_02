from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404