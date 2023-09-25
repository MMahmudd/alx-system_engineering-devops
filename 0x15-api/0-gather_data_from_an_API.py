#!/usr/bin/python3
"""Accessing_a REST API for_todo lists_of_employees"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_id

    response = requests.get(url)
    employee_Nme = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_Nme, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
