import random

ANIMAL_LIST = {'rabbit': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/1200px-Oryctolagus_cuniculus_Rcdo.jpg',
                'elephant':'https://static.scientificamerican.com/sciam/cache/file/065ACE5F-1E4B-4D3E-8E1E7CE0397D7681_source.jpg',
                'tiger':'https://i.natgeofe.com/n/6490d605-b11a-4919-963e-f1e6f3c0d4b6/sumatran-tiger-thumbnail-nationalgeographic_1456276.jpg',
                'panther':'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Jaguar.jpg/1200px-Jaguar.jpg',
                'pig': 'https://i.natgeofe.com/k/23e409f9-4699-46f0-a645-5cc1f5040363/pig-full-body.jpg?w=636&h=358'}


class PaperScissorsStone:
    """Class implementing a game (with memory)."""

    _results = ["It's a draw.", "I win!", 'You win!']

    def __init__(self, score=None):
        self.score = score or [0, 0]
        self.ANIMAL_LIST = ANIMAL_LIST

    def play_round(self, player_choice):
        """Play one round of Paper, Scissors, Stone, aka
        Rock paper scissors."""

        my_choice = random.randrange(0, 3)
        result = (my_choice-player_choice) % 3

        if result == 2:
            self.score[0] += 1
        elif result == 1:
            self.score[1] += 1

        return self._results[result], my_choice

    def reset(self):
        """Reset the score counter to zero."""
        self.score = [0, 0]
