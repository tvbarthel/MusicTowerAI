class Population:
    def __init__(self, players, generation):
        self.players = players
        self.generation = generation

    def get_players(self):
        return self.players

    def get_generation(self):
        return self.generation

    def get_average_score(self):
        score_sum = 0
        for player in self.players:
            score_sum += player.get_score()

        return score_sum / len(self.players)
