from Bot import Bot


class LocalBot(Bot):
    DEFAULT_TARGET_TIMESTAMP = [1100, 1900, 2700, 3470, 4277, 5040, 5853, 6611, 7418, 8200, 8999, 9791, 10569, 11332,
                                12118, 12906, 13710, 14471, 15233, 15999, 16793, 17621, 18387, 19134, 19909, 20689,
                                21468, 22191, 22956, 23718, 24445, 25153, 25897, 26633, 27405, 28115, 28817, 29526,
                                30241, 30978, 31719, 32478, 33256, 33977, 34688, 35434, 36126, 36832, 37551, 38246,
                                38972, 39675, 40358, 41048, 41726, 42454, 43119, 43784, 44437, 45094, 45769, 46441,
                                47105, 47774, 48453, 49123, 49797, 50442, 51104, 51752, 52406, 53054, 53693]

    DEFAULT_TOTAL_ERROR = 800

    def __init__(self, target_timestamp=DEFAULT_TARGET_TIMESTAMP, total_error=DEFAULT_TOTAL_ERROR):
        Bot.__init__(self)
        self.total_error = total_error
        deltas = []
        for index in range(len(target_timestamp)):
            deltas.append(
                target_timestamp[index] - target_timestamp[index - 1] if index > 0 else target_timestamp[index]
            )
        self.target_deltas = deltas

    def play(self, timestamps):
        if len(timestamps) > len(self.target_deltas):
            raise ValueError('LocalBot can only handle ' + str(len(self.target_deltas)) + ' timestamps ')

        score = 0
        error_left = 0
        error_right = 0
        for index in range(len(timestamps)):
            play_delta = timestamps[index] - timestamps[index - 1] if index > 0 else timestamps[index]
            error = abs(self.target_deltas[index] - play_delta)
            if index % 2 == 0:
                error_left += error
            else:
                error_right += error

            if error_left > self.total_error or error_right > self.total_error:
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
