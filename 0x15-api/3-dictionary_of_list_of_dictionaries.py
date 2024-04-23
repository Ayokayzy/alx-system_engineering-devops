#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
    )
    _obj = {}
    for user in users.json():
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user['id']}/todos"
        )
        tasks = todos.json()

        data = []
        for task in tasks:
            user_id = task['userId']
            task_title = task['title']
            task_status = task['completed']
            username = user['username']
            myobj = {
                'task': task_title,
                'completed': task_status,
                'username': username
            }
            data.append(myobj)
        _obj.update({user['id']: data})
    with open("todo_all_employees.json", 'w') as file:
        json.dump(_obj, file)
