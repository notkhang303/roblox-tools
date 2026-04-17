import json

class ConfigLoader:
    def __init__(self, default_config):
        # Load default configuration
        self.config = default_config

    def load_config(self, file_path):
        # Load configuration from a JSON file if it exists
        try:
            with open(file_path, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except FileNotFoundError:
            print(f'Config file not found: {file_path}')
        except json.JSONDecodeError:
            print(f'Error decoding JSON from: {file_path}')

    def get(self, key, default=None):
        # Retrieve a configuration value, with a default fallback
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    default_config = {
        'theme': 'dark',
        'language': 'en',
        'volume': 75
    }
    config_loader = ConfigLoader(default_config)
    config_loader.load_config('config.json')
    print(config_loader.get('theme'))  # Outputs the theme value
