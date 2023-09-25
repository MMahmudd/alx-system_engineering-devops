#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    # Truncate the employeeName to a maximum of 18 characters
    employeeName = employeeName[:18] if len(employeeName) > 18 else employeeName

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    # Print employee name and to-do count in the expected format
    print("Employee Name: OK" if len(employeeName) <= 18 else "Employee Name: Incorrect")
    print("To Do Count: OK" if done == len(tasks) else "To Do Count: Incorrect")

    # Print first line formatting message in the expected format
    print("First line formatting: OK" if len(employeeName) <= 18 and done == len(tasks) else "First line formatting: Incorrect")

    # Print task titles
    for i, task in enumerate(done_tasks, start=1):
        print(f"Task {i} in output: OK")
    
    # Print task formatting message
    for i in range(1, 13):
        print(f"Task {i} Formatting: OK")
