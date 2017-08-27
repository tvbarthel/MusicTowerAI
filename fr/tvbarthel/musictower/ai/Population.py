import math
from random import choice


class Population:
    # chance of mutation for each gene of a player.
    MUTATION_PERCENTAGE = 0.07

    # number of gene added once the generation is stable
    GROW_RATE = 5

    # score different allowed from the best player to be considered as a potential reproducer.
    REPRODUCER_SCORE_LOWER_RANGE_DELTA = 10

    def __init__(self, players, generation):
        self.players = players
        self.generation = generation

    def __str__(self):
        return "Generation : " + str(self.generation) + " ".join('\n' + (str(player)) for player in self.players)

    def get_players(self):
        return self.players

    def get_generation(self):
        return self.generation

    def get_average_score(self):
        score_sum = 0
        for player in self.players:
            score_sum += player.get_score()

        return score_sum / len(self.players)

    def get_max_score(self):
        score_max = 0
        for player in self.players:
            if score_max < player.get_score():
                score_max = player.get_score()

        return score_max

    def next_generation(self):
        # create pool
        pool = []

        # filter players to choose reproducers in the range of max_score
        # and max_score - REPRODUCER_SCORE_LOWER_RANGER_DELTA
        reproducers = []
        max_score = self.get_max_score()
        min_score = max_score
        for player in self.players:
            player_score = player.get_score()
            if max_score - player_score < self.REPRODUCER_SCORE_LOWER_RANGE_DELTA:
                reproducers.append(player)
                if player_score < min_score:
                    min_score = player_score

        for player in reproducers:
            score = player.get_score() - min_score + 1
            pool += int(math.pow(score, 4)) * [player]

        # reproduce players based on their fitness
        new_players = []
        size = len(self.players)
        for i in range(size):
            parent1 = choice(pool)
            parent2 = choice(pool)
            new_players.append(parent1.reproduce(parent2))

        # mutate new generation players
        for player in new_players:
            player.mutate(self.MUTATION_PERCENTAGE)

        # grow the next population if the current generation is stable enough
        if self.mustGrow():
            for player in new_players:
                player.add_genes(self.GROW_RATE)

        return Population(new_players, self.generation + 1)

    def mustGrow(self):
        """
        Used to determine if the population is enough stable to grow.
        Current implementation is based on players' score.
        If at least on player reach the max score, we must give him some space for improvement, grow!
        :return: true if the population must grow
        """
        maxScore = len(self.players[0].get_dna())
        mustGrow = False
        for player in self.players:
            if player.get_score() == maxScore:
                mustGrow = True
        return mustGrow
