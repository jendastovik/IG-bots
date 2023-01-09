import HTML
import json

def create(i):
    with open("bots.json", "r", encoding="utf8") as file:
        bots = json.load(file)
        
    for _ in range(i):
        bots["bots"].append(HTML.makeBot())

    with open("bots.json", "w", encoding="utf8") as file:
        file.write(json.dumps(bots))