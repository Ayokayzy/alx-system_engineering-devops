#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    employee_id = argv[1]

    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user = users.json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )
    tasks = todos.json()

    data = []
    for task in tasks:
        user_id = user['id']
        task_title = task['title']
        task_status = task['completed']
        username = user['username']
        myobj = {
            'task': task_title,
            'completed': task_status,
            'username': username
        }
        data.append(myobj)
    obj = { 'USER_ID': data }
    with open(f"{user['id']}.json", 'w') as file:
        json.dump(obj, file)
