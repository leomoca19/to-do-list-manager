"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user to-do list persists between sessions.
"""

from task import TaskManager
from utilities import welcome, goodbye, prompt, get_id


if __name__ == '__main__':
    TM = TaskManager()

    TM.load_from_file('tasks.txt')
    welcome()

    header = ('Exit 0 | View Tasks 1 | Add Task 2 | Update Task 3 | Delete Task 4\n'
              'Select an option')

    while answer := prompt(f'Tasks in system: {len(TM)}\n' + header, ['0', '1', '2', '3', '4']):
        match answer:
            case '0':
                answer = prompt('Are you sure you want to exit', ['y', 'n'])
                if answer == 'y':
                    break
            case '1':
                TM.view_tasks()
            case '2':
                TM.add_task(prompt('Enter a description of your new task'))
                print(f'Task added:{TM.tasks[-1]}')
            case '3':
                id = get_id('Select a Task ID: ')
                TM.update_task(id)
                print(f'Updated task:\n{TM.tasks[id]}')

            case '4':
                id = get_id('Select a Task ID: ')
                tmp = TM.remove_task(id)
                print(f'Deleted task:\n{TM.tasks[id]}')

    goodbye()
    TM.save_to_file('tasks.txt')
