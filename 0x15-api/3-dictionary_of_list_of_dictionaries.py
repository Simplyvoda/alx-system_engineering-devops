#!/usr/bin/python3
"""
This module contains a python script that exports data in JSON format
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    users_data = requests.get(url + "/users").json()

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "/todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users_data}, jsonfile)
