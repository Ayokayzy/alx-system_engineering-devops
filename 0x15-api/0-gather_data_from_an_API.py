#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""
import requests
from sys import argv


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
    completed_tasks = [
        task for task in tasks
        if task['completed'] == True
    ]
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(tasks)})")

    for task in completed_tasks:
        print("\t {}".format(task['title']))
