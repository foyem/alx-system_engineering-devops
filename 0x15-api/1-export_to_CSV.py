#!/usr/bin/python3
"""
export data in the CSV format
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":
    """ export data in the CSV format
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    filename = user_id + ".csv"

    employee = requests.get(url + 'users/' + user_id)
    employee = employee.json()

    task = requests.get(url + "todos?userId=" + user_id)
    task = task.json()

    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for counter in task:
            writer.writerow((counter.get('userId'), employee.get(
                'username'), counter.get('completed'), counter.get('title')))
