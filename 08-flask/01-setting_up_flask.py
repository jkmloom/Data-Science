# this code is for testing flask installation and environment files & settings
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print('home page!!')
    return "welcome to the flask app!"

if __name__ == "__main__":
    print('entering into the applicaiton')
    app.run(debug=True)