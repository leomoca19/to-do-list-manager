"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
"""

from task import TaskManager
from utilities import welcome, goodbye

DEBUG = True

if __name__ == '__main__':
    TM = TaskManager()

    welcome()

    if DEBUG:
        TM.add_sample_task(5)

    TM.update_task(1)

    goodbye()
