import datetime, json, random

from flask import Flask, redirect, render_template, request, session


app = Flask("The Note App")

app.secret_key = "hello"
# app.permanent_session_lifetime = datetime.timedelta(days=1)


@app.route("/", methods=["GET"])
def index():
    if "user" in session:
        username = session["user"]
        users = read_json()
        for user in users:
            if user["name"] == username:
                return render_template("/index.html", user_name=user["name"], user_notes=user["notes"])
    else:
        return redirect("/login")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("user-name").lower()
        users = read_json()
        session["user"] = username
        # session.permanent = True
        if len(users) == 0:
            return redirect("/new-user")
        else:
            for user in users:
                if username == user["name"]:
                    return redirect("/welcome")
                
            return redirect("/new-user")  
    else:
        return render_template("/login.html")


@app.route("/welcome")
def welcome():
    return render_template(
        "/welcome.html",
        user_name=session["user"],
    ), {"Refresh": "2; url=/"}


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/new-user")
def new_user():
    username = session["user"]
    new_user = create_user(username)

    users = read_json()
    users.append(new_user)

    write_json(users)
    return redirect('/welcome')


@app.route("/new-note", methods=["POST"])
def new_note():
    username = session["user"]
    content = request.form.get("note")
    users = read_json()
    for user in users:
        if (user["name"] == username):
            number_of_notes = len(user["notes"])
            note = create_note(number_of_notes, content)
            user["notes"].append(note)

    write_json(users)
    return redirect("/")
            

@app.route("/delete-note", methods=["GET", "POST"])
def delete():
    note_id = int(request.form.get("note-id"))
    users = read_json()
    for user in users:
        if user["name"] == session["user"]:
            filtered_notes = list(filter(lambda n: n["id"] != note_id, user["notes"]))
            user["notes"] = filtered_notes
            
    write_json(users)

    return redirect('/')



@app.route("/results")
def results():
    query = request.args.get("search").lower()
    users = read_json()
    results = []
    for user in users:
        if user["name"] == session["user"]:
            for note in user["notes"]:
                if note["content"].lower().find(query) != -1:
                    results.append(note)
            return render_template("/results.html", user_name=user["name"], results=results)


def create_user(name):
    return {"name": name, "notes": []}

def create_note(id, content):
    date = datetime.datetime.now()
    rand = random.randint(1, 7)
    color = "accent-" + str(rand)
    return {"id": id, "timestamp": date.strftime("%d %b %y %H:%M"), "content": content, "color": color}


def read_json():
    with open("./users.json", "r") as file:
        file_content = json.load(file)
    return file_content


def write_json(data):
    with open("./users.json", "w") as file:
        file.write(json.dumps(data, indent = 2))