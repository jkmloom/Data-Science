from flask import Flask, redirect, url_for

app = Flask('__main__')

@app.route("/")
def home():
    return "<h1>@jkmloom</h1><br>hello! this is the main page"

@app.route("/<name>")
def uesr(name):
    return f"hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()