import time

from Device import Device
from OCRManager import OCRManager


class Bot:
    """
    Encapsulate every logic used to instrument a game on a phone.
    """

    # 10 ms
    LOOP_DURATION_IN_SECONDS = 0.010

    # Coordinate to play very move without risking to restart the game in case of failure
    PLAY_COORDINATE_X = 410
    PLAY_COORDINATE_Y = 1530

    # Coordinate to trigger a new game and retrieve the original state of the app
    RESTART_COORDINATE_X = 540
    RESTART_COORDINATE_Y = 1340

    GAME_OVER_ANIMATION_DURATION_IN_SECONDS = 2

    def __init__(self):
        self.device = Device()
        self.OCRManager = OCRManager()
        pass

    def play(self, timestamps):
        """
        Perform a complete game from the loading screen
        Will play every move according to the given timestamp
        Then retrieve the score and redirect to the initial screen, ready for a new game
        :param timestamps: relative timestamp in milliseconds of each action. For instance (0, 1000, 1500)
        :return: score obtain at the end of the game.
        """

        # start playing
        start = self.get_current_time()
        self.device.touch(self.RESTART_COORDINATE_X, self.RESTART_COORDINATE_Y)

        # play every move
        for timestamp in timestamps:
            while timestamp > (self.get_current_time() - start):
                time.sleep(self.LOOP_DURATION_IN_SECONDS)
            self.device.touch(self.PLAY_COORDINATE_X, self.PLAY_COORDINATE_Y)

        # force game over in case reach the final score
        time.sleep(0.1)
        self.device.touch(self.PLAY_COORDINATE_X, self.PLAY_COORDINATE_Y)
        time.sleep(0.1)
        self.device.touch(self.PLAY_COORDINATE_X, self.PLAY_COORDINATE_Y)
        time.sleep(self.GAME_OVER_ANIMATION_DURATION_IN_SECONDS)

        # get score
        score = self.OCRManager.get_score(self.device)

        # go back to the loading screen
        self.device.touch(self.RESTART_COORDINATE_X, self.RESTART_COORDINATE_Y)

        return score

    def get_current_time(self):
        return int(round(time.time() * 1000))
