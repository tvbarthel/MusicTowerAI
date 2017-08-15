from random import choice, random


class Player:
    MUTATION_FACTORS = [-150, -100, -50, 50, 100, 150]

    def __init__(self, dna):
        self.dna = dna
        self.score = 0

    def get_score(self):
        return self.score

    def get_dna(self):
        return self.dna

    def reproduce(self, player):
        """
        Reproduce this player with another player.

        Note: no mutations occurs during the reproduction.
        See mutate().

        :param player: a player.
        :return: a newly created player.
        """
        first_parent_dna = self.get_dna()
        second_parent_dna = player.get_dna()
        child_dna = Player.__reproduce_dna(first_parent_dna, second_parent_dna)
        return Player(child_dna)

    def mutate(self, percentage):
        """
        Mutate this player.

        :param percentage: the percentage of mutation. Range [0,1]
        """
        if percentage < 0 or percentage > 1:
            raise ValueError("Percentage must be in range [0, 1]")
        dna_length = len(self.dna)
        for index in range(dna_length):
            if random() < percentage:
                mutation_factor = choice(Player.MUTATION_FACTORS)
                self.dna[index] += mutation_factor

    @staticmethod
    def __reproduce_dna(first_parent_dna, second_parent_dna):
        if len(first_parent_dna) is not len(second_parent_dna):
            raise ValueError("Player should have the same dna length")

        dna_length = len(first_parent_dna)
        child_dna = []
        for index in range(dna_length):
            if choice([True, False]):
                child_dna.append(first_parent_dna[index])
            else:
                child_dna.append(second_parent_dna[index])
        return child_dna
