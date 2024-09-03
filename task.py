from datetime import datetime

tasks = []


# Features to Implement:
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.


class Task:
    def __init__(self, description):
        self.description = description
        self.status = 'pending'
        self.date = datetime.now().date().strftime("%b-%d-%Y")

    def __str__(self):
        return f'{self.date} - {self.status}: {self.description}'


def view_tasks(status=None):
    """
    Display all current tasks with an option to view completed and pending tasks separately.
    """
    for task in tasks:
        if task:
            if status and status != task.status:
                continue
            print(task)
    print()


def add_task(task=None):
    """
    Adds a new tasks to the to-do list by prompting or argument
    """
    new_task = task if task else Task(input())
    tasks.append(new_task)


def update_task(id):
    """
    Allow the user to mark tasks as complete and edit the task details
    """
    if task := tasks[id]:
        print('Task selected: ')
        task.display()
        print()

        repeat = True
        while repeat:
            print('Mark as completed? y|n: ', end='')

            if answer := input().lower() in ['y', 'n']:
                repeat = False
                if answer == 'y':
                    task.status = 'completed'

            else:
                print('Bad input')

        repeat = True
        while repeat:
            print('Update description? y|n: ', end='')

            if input().lower() in ['y', 'n']:
                repeat = False
                print('New description: ', end='')
                task.description = input()

            else:
                print('Bad input')


def find_by_description(description):
    pass


def remove_task(id):
    """
    Deletes a task from the list by id
    """
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks[i] = None
            return


def save_to_file(file_name):
    """
    Saves tasks in a file
    """

    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(task)

    # with open(filename, 'w') as file:
    #     json.dump(tasks, file)


def load_from_file():
    """
    Loads tasks in a file
    """

    # global tasks
    # try:
    #     with open(filename, 'r') as file:
    #         tasks = json.load(file)
    # except FileNotFoundError:
    #     tasks = []
    pass
