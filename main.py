"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user’s to-do list persists between sessions.
"""

# tm stands for task manager
import task as tm

# Features to Implement:
# Save and Load Tasks: Persist tasks in a file so that they can be retrieved when the application is reopened.


def welcome():
    print('Welcome to a to-do list manager by Leonardo')


def goodbye():
    print('Goodbye!')


def print_(*string):
    """prints without a newline"""
    print(*string, end='')


def prompt(question, answers=None):
    """

    :param question: string to be displayed to ask for input
    :param answers: a list of the possible accepted answers, accepts any answer if None
    :return: the validated answer
    """

    print_(question)

    if answers:
        print_(answers[0])

        if answers[1]:
            for i in range(1, len(answers[1])):
                print_(answers[i], '|')

    print(question, answers, ':', end='')

    if answer := input().lower() in answers:
        pass


if __name__ == '__main__':
    welcome()

    for _ in range(3):
        tm.add_task()

    tm.view_tasks()
    tm.remove_task(2)
    tm.update_task(3)
    tm.view_tasks()

    goodbye()
