class Task:
    def __init__(self, id, description, status, date):
        self.id = id
        self.description = description
        self.status = status
        self.date = date

    def new_task(self):
        """
        prompts the user to create a new task
        :return: the new task from user input
        """
        pass


class TaskManager:
    def __init__(self):
        self.tasks = []

    def view_task(self, task):
        pass

    def add_task(self, task):
        pass

    def edit_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def save_to_file(self, task):
        pass

    def load_from_file(self, task):
        pass
