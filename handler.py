import json
from pathlib import Path

def load_roblox_data(file_path):
    """Load Roblox data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing Roblox data.

    Returns:
        dict: Parsed Roblox data.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_roblox_data(data, file_path):
    """Save Roblox data to a JSON file.

    Args:
        data (dict): Roblox data to save.
        file_path (str): Path to save the JSON file.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_roblox_data(file_path, new_data):
    """Update existing Roblox data with new information.

    Args:
        file_path (str): Path to the JSON file.
        new_data (dict): New data to merge into the existing data.

    Returns:
        dict: Updated Roblox data.
    """
    existing_data = load_roblox_data(file_path)
    existing_data.update(new_data)
    save_roblox_data(existing_data, file_path)
    return existing_data
