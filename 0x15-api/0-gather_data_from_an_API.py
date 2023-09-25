#!/usr/bin/python3
"""
Accessing a REST API for todo lists_of_employees
"""

import sys
import requests

def fetch_employee_todo_list(employee_id):
    """
    Fetches and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create the URL for fetching employee information
    employee_url = f"{base_url}/users/{employee_id}"

    # Create the URL for fetching employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todos_data if task.get("completed")]

        # Display the result
        print(f"Employee {employee_data.get('name')} is done with tasks"
              f"({len(completed_tasks)}/{len(todos_data)}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Failed to parse JSON data - {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
