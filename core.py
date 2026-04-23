import json
from typing import Any, Dict, Optional


def load_robox_data(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Load Roblox data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Optional[Dict[str, Any]]: Returns the parsed JSON data if successful, else None.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return None


def save_robox_data(data: Dict[str, Any], file_path: str) -> bool:
    """
    Save data to a JSON file in Roblox format.
    
    Args:
        data (Dict[str, Any]): The data to save.
        file_path (str): The path to the file where the data will be saved.
    
    Returns:
        bool: True if saving was successful, else False.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            return True
    except IOError as e:
        print(f"Error saving data: {e}")
        return False


def update_robox_data(existing_data: Dict[str, Any], new_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update existing Roblox data with new values.
    
    Args:
        existing_data (Dict[str, Any]): The original data to update.
        new_data (Dict[str, Any]): The new data to merge into the existing data.
    
    Returns:
        Dict[str, Any]: The updated data dictionary.
    """
    existing_data.update(new_data)
    return existing_data
