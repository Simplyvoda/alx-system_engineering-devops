#!/usr/bin/python3
"""
This module contains a python script that exports data in CSV format
"""
import csv
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_data = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    user_id = user_data.get('id')
    user_name = user_data.get('username')
    todo_res = requests.get(url + "/todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            csvwriter.writerow([user_id, user_name, todo.get('completed'),
                                    todo.get('title')])
