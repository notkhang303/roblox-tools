def validate_input(value):
    """
    Validates the input value to ensure it meets specified criteria.
    Only allows integers, and must be positive.
    """
    if not isinstance(value, int):
        raise ValueError('Input must be an integer.')
    if value <= 0:
        raise ValueError('Input must be a positive integer.')
    return True

if __name__ == '__main__':
    # Example use case in a loop
    inputs = [10, -5, 'abc', 20]
    for val in inputs:
        try:
            validate_input(val)
            print(f'Input {val} is valid.')
        except ValueError as e:
            print(f'Input {val} is invalid: {e}')