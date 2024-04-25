import requests

def get_employee_todo_progress(employee_id):
    # Replace this with the actual API endpoint for your TODO list service
    api_url = "https://api.example.com/todo-list/employees/{}/tasks".format(employee_id)

    response = requests.get(api_url)
    response_data = response.json()

    # Extract relevant information
    employee_name = response_data.get("employee_name")
    total_tasks = len(response_data.get("tasks"))
    done_tasks = sum(task.get("status") == "Done" for task in response_data.get("tasks"))

    # Print the progress
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in response_data.get("tasks"):
        if task.get("status") == "Done":
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
