from Bot import Bot


class LocalBot(Bot):
    DEFAULT_TARGET_DELTAS = [1100, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800,
                             700, 700, 700, 700, 700, 600, 600, 600, 700, 700, 800, 800, 900,
                             900, 900, 900, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]

    DEFAULT_TOTAL_ERROR = 800

    def __init__(self, target_deltas=DEFAULT_TARGET_DELTAS, total_error=DEFAULT_TOTAL_ERROR):
        Bot.__init__(self)
        self.target_deltas = target_deltas
        self.total_error = total_error

    def play(self, timestamps):
        if len(timestamps) > len(self.target_deltas):
            raise ValueError('LocalBot can only handle ' + str(len(self.target_deltas)) + ' timestamps ')

        score = 0
        error = 0
        for index in range(len(timestamps)):
            play_delta = timestamps[index] - timestamps[index - 1] if index > 0 else timestamps[index]
            error += abs(self.target_deltas[index] - play_delta)
            if error > self.total_error:
                return score
            else:
                score += 1

        return score


def test_local_bot():
    local_bot = LocalBot([1000, 1000, 1000, 1000], 200)

    score = local_bot.play([1000, 2000, 3000, 4000])
    assert score == 4, str(score) + ' != 4'

    score = local_bot.play([1100, 2100, 2950, 4000])
    assert score == 2, str(score) + ' != 2'

    score = local_bot.play([1100, 2050, 3050, 4150])
    assert score == 3, str(score) + ' != 3'

    score = local_bot.play([0, 2000])
    assert score == 0, str(score) + ' != 0'
