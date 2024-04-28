#!/usr/bin/python3
"""API task"""
import requests
import sys


if len(sys.argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]
    todo = requests.get(f"{url}users/{usr_id}/todos").json()
    res1 = requests.get(f"{url}users/{usr_id}").json()
    string = ""
    usr_name = res1["username"]
    for i in todo:
        completed = "True" if i["completed"] else "False"
        title = i["title"]
        string += f'"{usr_id}","{usr_name}","{i["completed"]}","{i["title"]}"\n'

    with open(f"{usr_id}.csv", "w") as csv:
        csv.write(string)
