from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/api")
def getTaskList()
    url = "https://api.todoist.com/"
    payload = {}
    files = {}
    
    response = requests.request("GET", url, data = payload, files = files)
    tasks = json.loads(response.text)
    
    for task in tasks:
        return task['content']

if __name__ == "__main__"
    app.run()