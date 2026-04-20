import json
import re
from validators import validate_user_input

class RobloxTools:
    def __init__(self):
        self.user_data = {}  

    def process_user_data(self, user_input):
        # Validate user input
        if not validate_user_input(user_input):
            raise ValueError('Invalid input. Please check your data.')

        # Process the validated user input
        self.user_data['username'] = user_input.get('username')
        self.user_data['age'] = user_input.get('age')
        self.user_data['email'] = user_input.get('email')
        print('User data processed successfully.')

    def to_json(self):
        return json.dumps(self.user_data)

# Example usage
if __name__ == '__main__':
    tools = RobloxTools()
    sample_input = {'username': 'RobloxPlayer1', 'age': 13, 'email': 'player@example.com'}
    try:
        tools.process_user_data(sample_input)
        print(tools.to_json())
    except ValueError as e:
        print(e)
