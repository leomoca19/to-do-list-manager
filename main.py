"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
"""

# tm stands for task manager
import task as tm
from utilities import welcome, goodbye

# Features to Implement:
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.


if __name__ == '__main__':
    welcome()

    for _ in range(3):
        tm.add_task()

    tm.view_tasks()
    tm.remove_task(2)
    tm.update_task(3)
    tm.view_tasks()

    goodbye()
