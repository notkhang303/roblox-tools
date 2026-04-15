import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config if default_config else {}
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(os.getcwd(), 'config.json')
        if os.path.isfile(config_path):
            with open(config_path, 'r') as config_file:
                user_config = json.load(config_file)
                return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        config_path = os.path.join(os.getcwd(), 'config.json')
        with open(config_path, 'w') as config_file:
            json.dump(self.config, config_file, indent=4)

# Example usage
if __name__ == '__main__':
    defaults = {'volume': 100, 'graphics': 'high'}
    config_loader = ConfigLoader(defaults)
    print(config_loader.get('volume'))  # Outputs the volume from the config
