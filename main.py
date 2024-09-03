"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
"""

from task import Task, add_task, view_tasks, update_task, remove_task
from utilities import welcome, goodbye

DEBUG = True

if __name__ == '__main__':
    welcome()
    t = Task('sample') if DEBUG else None

    for _ in range(3):
        add_task(t)

    view_tasks()
    remove_task(2)
    update_task(3)
    view_tasks()

    goodbye()
