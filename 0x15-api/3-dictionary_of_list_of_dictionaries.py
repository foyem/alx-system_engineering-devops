#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    """ obtain user and task completed from jsonplaceholder API
    """
    url = 'https://jsonplaceholder.typicode.com'
    filename = 'todo_all_employees.json'

    value1 = requests.get(url + '/todos')
    value2 = requests.get(url + '/users')
    a_dict = {}

    for user in value2.json():
        username = user.get('username')
        a_list = []
        for todo_dict in value1.json():
            if todo_dict.get('userId') == user.get('id'):
                task_dict = {}
                task_dict['task'] = todo_dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = todo_dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(user.get('id'))] = a_list

    with open(filename, 'w', newline='') as jsonfile:
        json.dump(a_dict, jsonfile)
