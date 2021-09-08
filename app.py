from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    '''Returns a welcome message'''

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html 

@app.get('/welcome/home')
def welcome_home():
    '''Returns a welcome home message'''

    html = "<html><body><h1>Welcome home</h1></body></html>"
    return html 

@app.get('/welcome/back')
def welcome_back():
    '''Returns a welcome back message'''

    html = "<html><body><h1>Welcome back</h1></body></html>"
    return html 