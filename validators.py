def validate_user_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if len(user_input) > 100:
        raise ValueError("Input cannot exceed 100 characters.")
    return user_input


def main_processing_loop():
    while True:
        user_input = input("Enter command: ")
        try:
            validated_input = validate_user_input(user_input)
            # Process the validated input
            print(f"Processing: {validated_input}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main_processing_loop()