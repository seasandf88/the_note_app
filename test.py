import json
from datetime import datetime

def new_user(name):
    return {"name": name, "notes": []}

def new_note(id, content, color):
    date = datetime.now()
    return {"id": id, "timestamp": date.strftime("%d %b %Y %H %M").split(" "), "content": content, "color": color}


user2 = new_user("Jane")

print(user2)
array = []


note2 = new_note("02", "This is my second note", "yellow")


user2["notes"].append(note2)

array.append(user2)


with open("./users.json", "w") as users_json:
  users_json.write(json.dumps(array))
  print("File printed")