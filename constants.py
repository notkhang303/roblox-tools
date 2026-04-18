class RobloxConstants:
    """
    Contains constants used throughout the Roblox tools.
    """
    GAME_URL = "https://www.roblox.com/games/"
    ASSET_URL = "https://www.roblox.com/asset/?id="
    API_ENDPOINT = "https://api.roblox.com/"
    MAX_PLAYER_COUNT = 100
    DEFAULT_GAMEMODE = "Classic"
    VALID_GAMEMODES = ["Classic", "Battle Royale", "Sandbox"]

    @staticmethod
    def get_game_url(game_id):
        """
        Generate full game URL from game ID.
        """
        return f"{RobloxConstants.GAME_URL}{game_id}"

    @staticmethod
    def get_asset_url(asset_id):
        """
        Generate full asset URL from asset ID.
        """
        return f"{RobloxConstants.ASSET_URL}{asset_id}"

    @staticmethod
    def is_valid_gamemode(gamemode):
        """
        Check if the provided gamemode is valid.
        """
        """
        return gamemode in RobloxConstants.VALID_GAMEMODES
