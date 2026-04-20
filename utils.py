import re


def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if not re.match(r'^[a-zA-Z0-9_]+$', user_input):
        raise ValueError("Input can only contain alphanumeric characters and underscores.")


def main_loop():
    while True:
        try:
            user_input = input('Enter your command: ')
            validate_input(user_input)
            # Process the valid input
            print(f'Processing command: {user_input}')
        except ValueError as e:
            print(f'Invalid input: {e}')

if __name__ == '__main__':
    main_loop()