"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user to-do list persists between sessions.
"""

from task import TaskManager
from utilities import welcome, goodbye, prompt, get_id


def run():
    tm = TaskManager()

    tm.load_from_file('tasks.txt')
    welcome()

    header = ('Exit 0 | View Tasks 1 | Add Task 2 | Update Task 3 | Delete Task 4\n'
              'Select an option')
    good_ans = ['0', '1', '2', '3', '4']

    while answer := prompt(f'Tasks in system: {len(tm)}\n' + header, good_ans):
        match answer:
            case '0':
                _header = 'Are you sure you want to save and exit'
                _good_ans = ['y', 'n']

                if prompt(_header, _good_ans) == 'y':
                    break
            case '1':
                tm.view_tasks()
            case '2':
                tm.add_task(prompt('Enter a description of your new task'))
                print(f'Task added:{tm.tasks[-1]}')
            case '3':
                id = get_id('Select a Task ID: ')
                print(f'Updated task:\n{tm.update_task(id)}')

            case '4':
                id = get_id('Select a Task ID: ')
                print(f'Deleted task:\n{tm.remove_task(id)}')

    goodbye()
    tm.save_to_file('tasks.txt')


if __name__ == '__main__':
    run()
