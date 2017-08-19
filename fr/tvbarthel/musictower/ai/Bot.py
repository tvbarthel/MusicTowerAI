class Bot:
    def __init__(self):
        pass

    def play(self, timestamps):
        """
        Perform a complete game from the loading screen
        Will play every move according to the given timestamp
        Then retrieve the score and redirect to the initial screen, ready for a new game
        :param timestamps: relative timestamp in milliseconds of each action. For instance (0, 1000, 1500)
        :return: score obtain at the end of the game.
        """
        raise NotImplementedError("You must implement this method in your subclass.")
