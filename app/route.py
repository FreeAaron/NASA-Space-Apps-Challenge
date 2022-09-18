from flask import render_template

def hello_world():
    return "Hello, MVC框架!"

def index():
    return render_template('index.html') 