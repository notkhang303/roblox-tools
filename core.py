import time
import functools

# Decorator to measure performance of functions

def performance_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f'[{func.__name__}] executed in {execution_time:.4f}s')
        return result
    return wrapper

# Sample usage of the performance monitor

class GameData:
    def __init__(self):
        self.players = []

    @performance_monitor
    def add_player(self, player_name):
        time.sleep(0.1)  # Simulate a delay
        self.players.append(player_name)

    @performance_monitor
    def get_player_count(self):
        time.sleep(0.1)  # Simulate a delay
        return len(self.players)

# Example of class usage
if __name__ == '__main__':
    game_data = GameData()
    game_data.add_player('Player1')
    count = game_data.get_player_count()
    print(f'Current player count: {count}')