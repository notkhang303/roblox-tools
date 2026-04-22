import json
import requests

class RobloxDataProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint):
        """Fetch data from the specified Roblox API endpoint."""
        response = requests.get(f'{self.api_url}/{endpoint}')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error fetching data: {response.status_code}')

    def process_user_data(self, user_id):
        """Process user data from Roblox API."""
        user_endpoint = f'users/{user_id}'
        user_data = self.fetch_data(user_endpoint)
        return {
            'id': user_data['id'],
            'username': user_data['username'],
            'join_date': user_data['created'],
            'status': user_data['lastStatus']
        }

    def process_game_data(self, game_id):
        """Process game data from Roblox API."""
        game_endpoint = f'games/{game_id}'
        game_data = self.fetch_data(game_endpoint)
        return {
            'id': game_data['id'],
            'name': game_data['name'],
            'genre': game_data['genre'],
            'visits': game_data['visits']
        }

if __name__ == '__main__':
    api_url = 'https://api.roblox.com'
    processor = RobloxDataProcessor(api_url)
    print(processor.process_user_data(1))  # Example user
    print(processor.process_game_data(1))  # Example game
