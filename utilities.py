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

    print_(question)

    # store the accepted answers
    answers_str = ''

    if answers:
        answers_str += answers[0]

        if answers[1]:
            for i in range(1, len(answers[1])):
                answers_str += (' | ' + answers[i])

    # display a character to show the user should input
    print_(': ')

    # validate answer
    if answer := input().lower() in answers:
        pass