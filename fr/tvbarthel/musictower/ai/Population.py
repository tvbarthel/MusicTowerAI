import math
from random import choice


class Population:
    # chance of mutation for each gene of a player.
    MUTATION_PERCENTAGE = 0.07

    # number of gene added once the generation is stable
    GROW_RATE = 5

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

    def next_generation(self):
        # create pool
        pool = []

        minScore = len(self.players[0].get_dna())
        for player in self.players:
            if player.get_score() < minScore:
                minScore = player.get_score()

        for player in self.players:
            score = player.get_score() - minScore + 1
            for i in range(int(math.pow(score, 4))):
                pool.append(player)

        # grow the population if the generation is stable enough
        if self.mustGrow():
            for player in self.players:
                player.add_genes(self.GROW_RATE)

        # reproduce players based on their fitness
        newPlayers = []
        size = len(self.players)
        for i in range(size):
            parent1 = choice(pool)
            parent2 = choice(pool)
            newPlayers.append(parent1.reproduce(parent2))

        # mutate new generation players
        for player in newPlayers:
            player.mutate(self.MUTATION_PERCENTAGE)

        return Population(newPlayers, self.generation + 1)

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
