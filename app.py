import datetime

from flask import Flask, redirect, render_template, request

app = Flask("The Note App")


@app.route("/")
def index():
    if request.method == "GET":
        name = "METHOD IS GET"
    else:
        name = "METHOD IS POST"

    return render_template("/index.html", name=name)


@app.route("/login")
def login():
    return render_template("/login.html")


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    name = "Fahed"
    return render_template(
        "/welcome.html",
        name=name,
    ), {"Refresh": "2; url=/"}
