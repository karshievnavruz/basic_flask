from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'Home Page!!'

@app.route('/uy')
def uy():
    return 'Home Page!!!!'

if __name__ == '__main__':
    
    app.run()