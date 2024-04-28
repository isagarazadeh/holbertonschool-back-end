#!/usr/bin/python3
"""API task"""
import requests
import sys

if len(sys.argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]
    todos = requests.get(f"{url}users/{usr_id}/todos").json()
    res1 = requests.get(f"{url}users/{usr_id}").json()
    string = ""
    usr_name = res1["username"]
    for i in todos:
        completed = "True" if i['completed'] else "False"
            title = i['title']
            csvfile.write(f'"{id}","{name}","{completed}","{title}"\n')

    with open(f"{usr_id}.csv", "w") as csv:
        csv.write(string)
