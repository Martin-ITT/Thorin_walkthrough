import os
from flask import Flask, render_template


"""
create an instance of Flask class
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
"""
app = Flask(__name__)

"""
In Python, a decorator starts with the @ symbol, which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.
"""
@app.route("/")
def index():
    #return "<h1>Hello, </h1> <h2>world</h2>"
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

"""
if name is equal to "main" (both wrapped in double underscores), then we're going to run our app with the following arguments.
The 'host' will be set to os.environ.get("IP"),
and I will set a default of "0.0.0.0".
We're using the os module from the standard library to get the 'IP' environment variable if it exists, but set a default value if it's not found.
It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", which is a common port used by Flask.
We also need to specify "debug=True", because that will allow us to debug our code much easier during the development stage.
The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.
This is the first one that we run, so if this has not been imported, which it won't be, then it's going to be run directly.
"""
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)