#!/usr/bin/python3
"""
This module contains a python script that uses REST API 
and returns a list of employee to do list
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ = "__main__":
    user_data = request.get(url + "/users/{}".format(sys.argv[1])).json()
    todo_res = request.get(url + "/todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()
    todo_done = []
    for i in todo_data:
        if todo_data["completed"] == true:
            todo_done.append(todo_data[i])


    print(
            "Employee {} is done with ({}/{}):".format(
                user_data.get('name'),
                len(todo_done),
                len(todo_data)
            )
        )
    for todo_done in todos_done:
        print('\t {}'.format(todo_done.get('title')))
