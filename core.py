import time
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(param):
    time.sleep(2)  # Simulated delay
    return f'Computed: {param}'

class GameData:
    def __init__(self):
        self.data = {}

    def get_data(self, key):
        if key not in self.data:
            self.data[key] = expensive_function(key)
        return self.data[key]

    def clear_data(self):
        self.data.clear()

if __name__ == '__main__':
    game_data = GameData()
    print(game_data.get_data('example'))
    print(game_data.get_data('example'))  # Should be instant on second call
    game_data.clear_data()
    print(game_data.get_data('example'))  # Will trigger computation again