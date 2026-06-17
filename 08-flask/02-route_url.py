from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello to the world that's not virtual</h1>"

@app.route('/hello') # doesn't have to match the name of the function
def hello():
    return "hello i'm mecatron! a machine."

@app.route('/greet/<name>')
def greet(name):
    return f"oh hey! hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
# default >> returns string; so we use syntax -> <int:variable_name>
def add(number1, number2):
    return f"do you know that : {number1} + {number2} = {number1 + number2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return "some parameters are missing!"

# --------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555, debug=True)