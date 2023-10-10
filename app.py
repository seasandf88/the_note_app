import datetime, json

from flask import Flask, redirect, render_template, request, session


app = Flask("The Note App")

app.secret_key = "hello"
app.permanent_session_lifetime = datetime.timedelta(days=1)


@app.route("/", methods=["GET", "POST"])
def index():
    if "user" in session:
        user = session["user"]
        return render_template("/index.html", user_name=user)
    else:
        return redirect("/login")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user_name")
        session["user"] = user
        session.permanent = True
        return redirect("/new-user")
    else:
        return render_template("/login.html")


@app.route("/welcome")
def welcome():
    user = session["user"]    
    return render_template(
        "/welcome.html",
        user_name=user,
    ), {"Refresh": "2; url=/"}


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/new-user")
def new_user():
    username = session["user"]
    user = create_user(username)
    with open("./users.json", "r") as file:
        users = json.load(file)
        users.append(user)

    with open("./users.json", "w") as file:
        file.write(json.dumps(users))
    return redirect('/welcome')




def create_user(name):
    return {"name": name, "notes": []}

def create_note(id, content, color):
    date = datetime.now()
    return {"id": id, "timestamp": date.strftime("%d %b %Y %H %M").split(" "), "content": content, "color": color}
