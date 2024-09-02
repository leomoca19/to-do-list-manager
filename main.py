'''
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
'''

from datetime import datetime

# Features to Implement:
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.

DEBUG = True
tasks = []


class Task:
    def __init__(self, description):
        self.id = len(tasks) + 1
        self.description = description
        self.status = 'pending'
        self.date = datetime.now().date().strftime("%b-%d-%Y")

    def display(self):
        print('-' * (len(self.description) + 14))
        print('Task ID:', self.id)
        print(self.date, '-', self.description)
        print(self.status)


def welcome():
    print('Welcome to a to-do list manager by Leonardo')


def goodbye():
    print('Goodbye!')


def view_tasks(status=None):
    """
    Display all current tasks with an option to view completed and pending tasks separately.
    """
    print()
    for task in tasks:
        if task:
            if status and status != task.status:
                continue
            task.display()
    print()


def add_task(task=None):
    """
    Adds a new tasks to the to-do list by prompting or argument
    """

    if task:
        tasks.append(task)

    else:
        description = input() if not DEBUG else 'sample'
        tasks.append(Task(description))


def update_task():
    pass


def remove_task(id):
    """
    Deletes a task from the list by id
    """
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks[i] = None
            return

        tasks.append(new_task)




if __name__ == '__main__':
    welcome()
    goodbye()
