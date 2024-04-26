#!/usr/bin/python3
"""tasks 1"""
import requests


def get_employee_todo_progress(employee_id):

    api_url = "https://api.example.com/employees/{}/tasks".format(employee_id)
    response = requests.get(api_url)
    response_data = response.json()
    name = response_data.get("employee_name")
    total_tasks = len(response_data.get("tasks"))
    done_tasks = sum(task.get("status") == "Done")
    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}): ")

    for task in response_data.get("tasks"):
        if task.get("status") == "Done":
            print(f"\t{task.get('title')}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
