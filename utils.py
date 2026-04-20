import os
import json
import logging

def load_settings(file_path):
    """Load settings from a JSON file."""
    if not os.path.exists(file_path):
        logging.error(f"Settings file {file_path} not found.")
        return None
    with open(file_path, 'r') as file:
        return json.load(file)


def save_settings(file_path, settings):
    """Save settings to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(settings, file, indent=4)
    logging.info(f"Settings saved to {file_path}.")


def validate_setting(setting, valid_types):
    """Validate setting against allowed types."""
    if not isinstance(setting, valid_types):
        logging.error(f"Invalid setting type: {type(setting).__name__}.")
        return False
    return True


def create_directory(directory_path):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        logging.info(f"Directory created: {directory_path}.")
    else:
        logging.info(f"Directory already exists: {directory_path}.")
