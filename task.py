from datetime import datetime

# Features to Implement:
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.


class TaskManager:
    class Task:
        def __init__(self,
                     id,
                     description,
                     status='pending',
                     date=datetime.now().date().strftime("%b-%d-%Y")):
            self.id = id
            self.description = description
            self.status = status
            self.date = date

        def __str__(self):
            return f'ID: {self.id} - {self.description}\n{self.date} - {self.status}\n'

    def __init__(self, id_counter=1):
        self.id_counter = id_counter
        self.tasks = []

    def find_by_id(self, id):
        """
        :param id: the task id
        :return: index of the task with the given id
        """

        for i, task in enumerate(self.tasks):
            if task.id > id:
                return None

            if task.id == id:
                return i

    def add_sample_task(self, x):
        """
        adds x sample tasks
        """

        s = self
        for i in range(x):
            s.tasks.append(s.Task(s.id_counter, 'sample'))
            s.id_counter += 1

    def view_tasks(self, status=None):
        """
        Display all current tasks with an option to view completed and pending tasks separately.
        """

        if len(self.tasks):
            for task in self.tasks:
                if task:
                    if status and status != task.status:
                        continue
                    print(task)

        else:
            print('No tasks')

    def add_task(self, task=None):
        """
        Adds a new tasks to the to-do list by prompting or argument
        """
        new_task = task if task else self.Task(self.id_counter, input())
        self.id_counter += 1

        self.tasks.append(new_task)

    def update_task(self, id):
        """
        Allow the user to mark tasks as complete and edit the task details
        """
        if task := self.tasks[id]:
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

    def remove_task(self, id):
        """
        Deletes a task from the list by id
        """

        task = self.tasks[i := 0]
        while task and task.id <= id:
            if task.id == id:
                self.tasks.remove(task)
                return

            i += 1
            task = self.tasks[i]

        print('Task ID not found')

    def save_to_file(self, file_name):
        """
        Saves tasks in a file
        """

        with open(file_name, 'w') as file:
            for task in self.tasks:
                file.write(task)

    def load_from_file(self, ):
        """
        Loads tasks from a file
        """

        with open(file_name, 'r') as file:
            line = file.readline()

            # discard 'ID: '
            line = line[4:-1]

            # read ID
            id = line[:2]

            # discard ' - '
            line = line[2:]

            # read description without '\n'
            description = line

            line = file.readline()
            status = ''
            date = ''

            self.add_task(self.Task(id, description, status, date))
