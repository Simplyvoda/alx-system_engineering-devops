#!/usr/bin/python3
"""
This module contains a python script that exports data in JSON format
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_data = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    user_id = user_data.get('id')
    user_name = user_data.get('username')
    todo_res = requests.get(url + "/todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()

    with open("{}.json".format(user_id), 'w') as jsonfile:
            json.dump({user_id: [{
                "task" : todo.get('title'),
                "completed" : todo.get('completed'),
                "username" : user_name
                } for todo in todo_data]}, jsonfile)
