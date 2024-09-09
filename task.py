from datetime import datetime
from utilities import prompt


class TaskManager:
    class Task:
        def __init__(self,
                     id,
                     description,
                     status='pending',
                     date=datetime.now().date().strftime("%b-%d-%Y")):
            self.id = id
            self.description = description
            self.date = date
            self.status = status

        def __str__(self):
            return f'ID: {self.id} - {self.description}\n{self.date} - {self.status}\n'

    def __init__(self, id_counter=1):
        self.id_counter = id_counter
        self.tasks = []

    def __len__(self):
        return len(self.tasks)

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

    def add_task(self, description):
        """
        Adds a new tasks to the to-do list by prompting or argument
        """
        self.tasks.append(self.Task(self.id_counter, description))
        self.id_counter += 1

    def update_task(self, id):
        """
        Allow the user to mark tasks as complete and edit the task details
        """

        i = self.find_by_id(id)
        if i is not None:
            task = self.tasks[i]
            print(f'Task selected: {task}')

            answer = prompt('Mark as completed?', ['y', 'n'])
            if answer == 'y':
                task.status = 'completed'

            answer = prompt('Update description?', ['y', 'n'])
            if answer == 'y':
                task.status = input('Enter new description:')

        else:
            print('Task not found')

    def remove_task(self, id):
        """
        Deletes a task from the list by id
        :return: the deleted task
        """

        i = self.find_by_id(id)
        if i is not None:
            tmp = self.tasks[i]
            del self.tasks[i]
            return tmp
        else:
            print('Task ID not found')

    def save_to_file(self, file_name):
        """
        Saves tasks in a file
        """

        with open(file_name, 'w') as file:
            for task in self.tasks:
                file.write(str(task))
            file.write('last id: ' + str(self.id_counter) + '\n')

    def load_from_file(self, file_name):
        """
        Loads tasks from a file
        """

        with open(file_name, 'r') as file:

            while line := file.readline():

                # if this is the last line of the file, stop reading
                if line[:9] == 'last id: ':
                    self.id_counter = int(line[9:])
                    break

                skip_str = 4  # discard 'ID: '
                empty_pos = line.find(' ', skip_str)

                id = int(line[skip_str:empty_pos])  # read ID
                description = line[empty_pos + 3:-1]  # discard ' - ', '\n' and read description

                line = file.readline()
                empty_pos = line.find(' ')

                date = line[:empty_pos]  # read date
                status = line[empty_pos + 3:-1]  # discard ' - ' and '\n' and read status

                new_task = self.Task(id, description, status, date)
                self.tasks.append(new_task)
