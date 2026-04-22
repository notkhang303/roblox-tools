import random


def generate_random_id(length=12):
    """Generate a random string of fixed length"
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


def format_time(seconds):
    """Convert seconds to a human-readable format"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours}h {minutes}m {seconds}s'


def clamp(value, min_value, max_value):
    """Restrict a value to a given range"
    return max(min(value, max_value), min_value)


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def read_json_file(filepath):
    """Read a JSON file and return its content"""
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json_file(filepath, data):
    """Write data to a JSON file"""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
