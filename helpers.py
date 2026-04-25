def calculate_player_score(player_data):
    """
    Calculate the score of a player based on their actions
    in the game.
    """
    score = 0
    for action in player_data['actions']:
        score += action['points']
    return score


def generate_random_id(length=8):
    """
    Generate a random alphanumeric ID of given length.
    """
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def format_timestamp(timestamp):
    """
    Convert a timestamp into a human-readable date string.
    """
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def validate_player_data(player_data):
    """
    Validate the structure of player data dictionary.
    """
    required_keys = ['id', 'name', 'level', 'actions']
    return all(key in player_data for key in required_keys)


def filter_active_players(player_list):
    """
    Filter the active players from a list based on their status.
    """
    return [player for player in player_list if player['status'] == 'active']
