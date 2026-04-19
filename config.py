import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path)
        if user_config:
            config.update(user_config)
        return config

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get('some_key', 'default_value'))