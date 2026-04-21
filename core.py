from typing import List, Dict, Any

class RobloxGame:
    """
    Represents a Roblox game with various attributes.
    """

    def __init__(self, title: str, genre: str, player_count: int) -> None:
        """
        Initializes a new instance of RobloxGame.
        
        :param title: The title of the game.
        :param genre: The genre of the game.
        :param player_count: The current number of players in the game.
        """
        self.title = title
        self.genre = genre
        self.player_count = player_count

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the game attributes to a dictionary.
        
        :return: A dictionary representation of the game.
        """
        return {
            'title': self.title,
            'genre': self.genre,
            'player_count': self.player_count
        }

    def update_player_count(self, count: int) -> None:
        """
        Updates the player count of the game.
        
        :param count: The new player count.
        """
        self.player_count = count

def get_top_games(games: List[RobloxGame]) -> List[RobloxGame]:
    """
    Returns a list of Roblox games sorted by player count.
    
    :param games: A list of RobloxGame instances.
    :return: A list of Roblox games sorted by player count in descending order.
    """
    return sorted(games, key=lambda game: game.player_count, reverse=True)
