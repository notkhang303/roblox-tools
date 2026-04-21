import json
from typing import Any, Dict


def load_roblox_data(file_path: str) -> Dict[str, Any]:
    """
    Load JSON data from a Roblox data file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Dict[str, Any]: The loaded data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from: {file_path}')
    return {}


def save_roblox_data(file_path: str, data: Dict[str, Any]) -> None:
    """
    Save a dictionary as JSON to a Roblox data file.
    
    Args:
        file_path (str): The path where to save the data.
        data (Dict[str, Any]): The data to save.
    
    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'Data successfully saved to: {file_path}')
    except IOError:
        print(f'Error writing to file: {file_path}')