# this code is for testing flask installation and environment files & settings
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "welcome to the flask app!"

if __name__ == "__main__":
    app.run(debug=True)