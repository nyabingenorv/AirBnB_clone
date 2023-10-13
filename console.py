#!/usr/bin/python3
'''Running point for CMD loop'''
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
    user_input = input(cmd)
    # Help and closing Decision
    if user_input == 'help':
        print(message)
    elif user_input == 'quit':
        controller = 0
