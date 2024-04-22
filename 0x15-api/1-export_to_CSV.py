#!/usr/bin/python3
"""
1-export_to_CSV.py
"""
import csv
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
Export to CSV
    with open(f'{employee_id}.csv', 'w') as file:
        writer = csv.writer(file, dialect="unix", delimiter=",")
        for task in tasks:
            row = [employee_id, user['name'], task['completed'], task['title']]
            writer.writerow(row)
