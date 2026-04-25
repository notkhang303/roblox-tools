import json
import time

class RobloxProcessor:
    def __init__(self, game_id):
        self.game_id = game_id
        self.player_data = []

    def log_player_event(self, player_id, event_type):
        event = {
            'player_id': player_id,
            'event_type': event_type,
            'timestamp': time.time()
        }
        self.player_data.append(event)

    def get_events_json(self):
        return json.dumps(self.player_data, indent=4)

    def clear_events(self):
        self.player_data.clear()

    def print_summary(self):
        print(f'Game ID: {self.game_id}')
        print(f'Total Events: {len(self.player_data)}')
        for event in self.player_data:
            print(f"Player {event['player_id']} triggered {event['event_type']} at {event['timestamp']}.")

# Example usage
if __name__ == '__main__':
    processor = RobloxProcessor(game_id=123456)
    processor.log_player_event(player_id='player1', event_type='joined')
    processor.log_player_event(player_id='player2', event_type='left')
    processor.print_summary()