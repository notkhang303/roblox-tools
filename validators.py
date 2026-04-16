def validate_input(data):
    """
    Validate input data for processing.
    
    Parameters:
    data (dict): The input data to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    required_fields = ['username', 'game_id', 'action']
    
    for field in required_fields:
        if field not in data:
            print(f'Missing required field: {field}')
            return False
        if not data[field]:
            print(f'Field {field} cannot be empty')
            return False

    if not isinstance(data['game_id'], int) or data['game_id'] <= 0:
        print('Game ID must be a positive integer')
        return False

    if data['action'] not in ['join', 'leave', 'play']:
        print('Invalid action type')
        return False

    return True


if __name__ == '__main__':
    sample_input = {'username': 'Player1', 'game_id': 123, 'action': 'join'}
    is_valid = validate_input(sample_input)
    print('Input Valid:', is_valid)