import random
import logging

logger = logging.getLogger(__name__)

class GameSession:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        logger.info(f"Initialized game session for {player_name}")

    def update_score(self, points):
        self.score += points
        logger.info(f"{self.player_name} scored {points} points. Total score: {self.score}")

    def get_score(self):
        return self.score

    def end_session(self):
        logger.info(f"Ending game session for {self.player_name}. Final score: {self.score}")

class Game:
    def __init__(self):
        self.sessions = []

    def start_session(self, player_name):
        session = GameSession(player_name)
        self.sessions.append(session)
        logger.info(f"Started new session for {player_name}")
        return session

    def simulate_game(self):
        for session in self.sessions:
            points = random.randint(1, 10)
            session.update_score(points)

    def end_all_sessions(self):
        for session in self.sessions:
            session.end_session()

if __name__ == '__main__':
    game = Game()
    player1 = game.start_session('Player1')
    player2 = game.start_session('Player2')
    game.simulate_game()
    game.end_all_sessions()
