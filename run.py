import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


"""
create an instance of Flask class
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
"""
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title ="About", company=data, list_of_numbers=[1, 2, 3])


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    if request.method == "POST":
        print(request.form)
        print(request.form.get("name"))
        print(request.form["email"])
    """
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title ="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title ="Careers")

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