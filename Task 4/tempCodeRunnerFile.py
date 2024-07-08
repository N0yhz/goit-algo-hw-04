from parse import parse_input
from actions import add_contacts,  change_contacts, show_phone, handle_command

if __name__ == '__main__':
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        result = handle_command(command,args)
        print(result)
        if command in {'close', 'exit'}:
            break