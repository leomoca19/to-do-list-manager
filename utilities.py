def welcome():
    print('Welcome to a to-do list manager by Leonardo')


def goodbye():
    print('Goodbye!')


def print_(*string):
    """
    prints without a newline
    """
    print(*string, end='')


def prompt(question, answers=None):
    """
    displays the question, then prompts the user to input an answer and validates the input

    :param question: string to be displayed to ask for input
    :param answers: a list of the possible accepted answers, accepts any answer if None
    :return: the validated answer
    """

    full_str = question

    # add possible answers
    if answers:
        full_str += ' ' + '|'.join(answers)

    # character to show the user should input
    full_str += ': '

    # validate answer
    while True:
        print(full_str)

        if answers:
            return input()

        if (answer := input()) in answers:
            return answer

        print('Bad input')

