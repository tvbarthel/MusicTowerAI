from Bot import Bot


class LocalBot(Bot):
    def __init__(self, timestamps, total_error):
        Bot.__init__(self)
        self.timestamps = timestamps
        self.total_error = total_error

    def play(self, timestamps):
        if len(timestamps) > len(self.timestamps):
            raise ValueError('LocalBot can only handle ' + str(len(self.timestamps)) + ' timestamps ')

        score = 0
        error = 0
        for index, candidate_timestamp in enumerate(timestamps):
            error += abs(candidate_timestamp - self.timestamps[index])
            if error > self.total_error:
                return score
            else:
                score += 1

        return score


def test_local_bot():
    local_bot = LocalBot([1000, 2000, 3000, 4000], 200)

    score = local_bot.play([1000, 2000, 3000, 4000])
    assert score == 4, str(score) + ' != 4'

    score = local_bot.play([1100, 1900, 2950, 4000])
    assert score == 2, str(score) + ' != 2'

    score = local_bot.play([1100, 1900, 3000, 4010])
    assert score == 3, str(score) + ' != 3'

    score = local_bot.play([0, 2000])
    assert score == 0, str(score) + ' != 0'
