import datetime

from flask import Flask, redirect, render_template, request

app = Flask("The Note App")


@app.route("/")
def index():
    test = "Hello User"
    return render_template("/login.html", test=test)
