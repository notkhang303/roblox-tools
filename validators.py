def is_valid_user_id(user_id):
    """
    Validate if the user ID is in the correct format.
    User IDs should be numeric and positive.
    """
    return isinstance(user_id, int) and user_id > 0


def is_valid_game_id(game_id):
    """
    Validate if the game ID is in the correct format.
    Game IDs should be numeric and positive.
    """  
    return isinstance(game_id, int) and game_id > 0


def is_valid_username(username):
    """
    Validate if the username is in the correct format.
    Usernames should be a string of 3 to 20 alphanumeric characters.
    """
    if not isinstance(username, str):
        return False
    return 3 <= len(username) <= 20 and username.isalnum()


def is_valid_asset_id(asset_id):
    """
    Validate if the asset ID is in the correct format.
    Asset IDs should be numeric and positive.
    """  
    return isinstance(asset_id, int) and asset_id > 0


def is_valid_email(email):
    """
    Validate if the email address is properly formatted.
    This uses a simple regex pattern.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
