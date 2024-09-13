"""
Simple command-line application to manage tasks, including adding, updating, deleting, and displaying tasks.
The tasks will be stored in a local file so that the user to-do list persists between sessions.
"""
import sys
sys.path.append('C:/source/to-do-list-manager')

from task import run

if __name__ == '__main__':
    run()
