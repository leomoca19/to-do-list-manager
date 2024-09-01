'''
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
'''

from datetime import datetime


# Features to Implement:
# Add Task: Allow users to add new tasks to the to-do list.
# View Tasks: Display all current tasks with an option to view completed and pending tasks separately.
# Update Task: Enable users to mark tasks as complete or edit the task details.
# Delete Task: Allow users to delete tasks from the list.
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.

DEBUG = True

def welcome():
    print('Welcome to my to-do list manager by Leonardo')


def goodbye():
    print('Goodbye!')


if __name__ == '__main__':
    welcome()
    goodbye()
