import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'max_players': 20,
    'game_mode': 'survival',
    'difficulty': 'normal',
}

class ConfigLoader:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                return self._merge_with_defaults(json.load(file))
        return DEFAULT_CONFIG

    def _merge_with_defaults(self, user_config):
        # Merge user config with defaults
        config = DEFAULT_CONFIG.copy()
        config.update(user_config)
        return config

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)
