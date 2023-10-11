import datetime, json, random

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

# required secret key for the session functionality
app.secret_key = "hello"


@app.route("/", methods=["GET"])
def index():
    if "user" in session:
        # reads the users.json file and puts the list inside users variable
        users = read_json()
        for user in users:
            # match the logged in user with the existing users
            if user["name"] == session["user"]:
                # if the user exists redirect to homepage
                return render_template(
                    "/index.html", user_name=user["name"], user_notes=user["notes"]
                )
    else:
        # if it's a new user, redirect to login 
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = read_json()
        # store a lower cased user name inside session["user"]
        session["user"] = request.form.get("user-name").lower() 
        # if there are no users, redirect to /new-user
        if len(users) == 0:
            return redirect("/new-user")
        else:
            for user in users:
                if session["user"] == user["name"]:
                    # if the user exists, redirect to /welcome
                    return redirect("/welcome")

            # if the user doesn't exist redirect to create an new user
            return redirect("/new-user")
    else:
        # just render the page if the request method id GET
        return render_template("/login.html")


@app.route("/welcome")
def welcome():
    return render_template(
        "/welcome.html",
        user_name=session["user"],
    ), {"Refresh": "2; url=/"} # redirect to homepage after 2 seconds


@app.route("/logout")
def logout():
    session.clear() # clear the session storage then redirect to login page
    return redirect("/login")


@app.route("/new-user") 
def new_user():
    new_user = create_user(session["user"]) # creates new user dictionary

    users = read_json() # put the users inside an array
    users.append(new_user) # append the new user to the array 

    write_json(users) # write the new array to file
    return redirect("/welcome")


@app.route("/new-note", methods=["POST"])
def new_note():
    content = request.form.get("note") # get the note content from the form
    users = read_json()
    for user in users:
        if user["name"] == session["user"]:
            # get the number of notes for the current user
            number_of_notes = len(user["notes"])
            # creates a new note with the index and content as arguments
            note = create_note(number_of_notes, content)
            # append the new note to the user's notes array
            user["notes"].append(note)

    write_json(users) # rewrite the json file
    return redirect("/")


@app.route("/delete-note", methods=["POST"])
def delete():
    note_id = int(request.form.get("note-id")) # store the note index
    users = read_json()
    for user in users:
        if user["name"] == session["user"]:
            # filtering out the note that match the id
            filtered_notes = list(filter(lambda note: note["id"] != note_id, user["notes"]))
            # update the user notes array
            user["notes"] = filtered_notes

    write_json(users)

    return redirect("/")


@app.route("/results")
def results():
    # get the search query from the form search field
    query = request.args.get("search").lower()
    users = read_json()
    results = [] # empty results array
    for user in users:
        if user["name"] == session["user"]: # match the user name
            for note in user["notes"]: # loop through user notes
                # this evaluate to true if a match was found
                if note["content"].lower().find(query) != -1:
                    # append the matched note to the results array
                    results.append(note)
            return render_template(
                "/results.html", user_name=user["name"], results=results
            )


# creates a dict for the new user
def create_user(name):
    return {"name": name, "notes": []}


# create a dict for the new note
def create_note(id, content):
    date = datetime.datetime.now()
    # generates a random number between 1 and 7
    rand = random.randint(1, 7)
    color = "accent-" + str(rand)
    return {
        "id": id,
        "timestamp": date.strftime("%d %b %y %H:%M"),
        "content": content,
        "color": color,
    }


# reads and returns the users.json content as an array
def read_json():
    with open("./users.json", "r") as file:
        file_content = json.load(file)
    return file_content


# writes the passed array to the users.json file
def write_json(data):
    with open("./users.json", "w") as file:
        file.write(json.dumps(data, indent=2))
