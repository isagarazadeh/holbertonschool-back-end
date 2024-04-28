#!/usr/bin/python3
"""API task"""
import json
import requests
import sys

if len(sys.argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]
    dictionary = {f"{usr_id}": []}
    todo = requests.get(f"{url}users/{usr_id}/todos").json()
    res1 = requests.get(f"{url}users/{usr_id}").json()
    name = res1["username"]
    string = ""
    for i in todo:
        new_dict = {}
        new_dict["task"] = i["title"]
        new_dict["completed"] = i["completed"]
        new_dict["username"] = name
        dictionary[f"{usr_id}"].append(new_dict)

    with open(f"{usr_id}.json", "w") as jsonfile:
        json.dump(dictionary, jsonfile))
