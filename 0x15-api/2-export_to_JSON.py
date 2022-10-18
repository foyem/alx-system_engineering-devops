#!/usr/bin/python3
"""
export data in the JSON format
"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    """ export data in the JSON format
    """
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    filename = user_id + ".json"

    value1 = requests.get(url + '/todos')
    value2 = requests.get(url + '/users/{}'.format(user_id))
    username = value2.json()['username']

    with open(filename, 'w', newline='') as csvfile:
        a_dict = {}
        a_list = []
        for todo_dict in value1.json():
            if todo_dict.get('userId') == int(user_id):
                task_dict = {}
                task_dict['task'] = todo_dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = todo_dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(user_id)] = a_list
        json.dump(a_dict, csvfile)
