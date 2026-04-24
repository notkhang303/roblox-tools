# handler.py

import json
import requests

class RobloxAPIHandler:
    BASE_URL = "https://api.roblox.com/"

    @staticmethod
    def get_user_info(user_id):
        """Fetch user information by user ID."""
        response = requests.get(f"{RobloxAPIHandler.BASE_URL}users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def get_game_info(game_id):
        """Fetch game information by game ID."""
        response = requests.get(f"{RobloxAPIHandler.BASE_URL}games/{game_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def get_user_friends(user_id):
        """Fetch friends for a specific user by user ID."""
        response = requests.get(f"{RobloxAPIHandler.BASE_URL}users/{user_id}/friends")
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Example usage:
# user_info = RobloxAPIHandler.get_user_info(123456)
# print(json.dumps(user_info, indent=4))
