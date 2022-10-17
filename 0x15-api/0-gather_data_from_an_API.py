#!/usr/bin/python3
"""
This module contains a python script that uses REST API 
and returns a list of employee to do list
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_data = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todo_res = requests.get(url + "/todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()
    todo_done = [t.get("title") for t in todo_data if t.get("completed") is True]

    print(
            "Employee {} is done with ({}/{}):".format(
                user_data.get('name'),
                len(todo_done),
                len(todo_data)
            )
        )
    [print("\t {}".format(c)) for c in todo_done]
