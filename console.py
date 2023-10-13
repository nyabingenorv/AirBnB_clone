#!/usr/bin/python3
'''Running point for CMD loop'''


def main_runner():
    '''console runner'''
    # message to display
    cmd = '(hbnb)'

    message = '''Documented commands (type help <topic>):
    ========================================
    EOF  help  quit'''
    # main loop controller
    controller = 1
    # buffer for user input
    user_input = ''
    while controller:
        # Taking user input
        user_input = input(cmd).lower()
        # Help and closing Decision
        if user_input == 'help':
            print(message)
        elif user_input == 'quit':
            controller = 0


if __name__ == "__main__":
    main_runner()
