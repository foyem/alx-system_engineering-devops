#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ Return employees and task
    """

    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    employee1 = requests.get(url + 'users/' + user_id)
    employee = employee1.json()

    task1 = requests.get(url + "todos?userId=" + user_id)
    task = task1.json()

    list_task_done = []
    for counter in task:
        if counter.get("completed") is True:
            list_task_done.append(counter)
    task_done = len(list_task_done)
    task_total = len(task)
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), task_done, task_total))
    for count in list_task_done:
        print('\t {}'.format(count.get('title')))
