from random import choice, random, randint


class Player:
    MUTATION_FACTORS = [-100, -75, -50, 50, 75, 100]
    NEW_GENE_DEFAULT_OFFSET = 1000
    NEW_GENE_MIN_VARIATION = -200
    NEW_GENE_MAX_VARIATION = 200

    def __init__(self, dna):
        self.dna = dna
        self.score = 0

    def __str__(self):
        return "Score : " + str(self.score) + " " + str(self.dna)

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
                self.dna[index] = max(0, self.dna[index] + mutation_factor)

    def add_genes(self, number_of_genes_to_add):
        """
        Add new genes to this player.

        :param number_of_genes_to_add: the number of genes to add.
        """
        if number_of_genes_to_add <= 0:
            raise ValueError("The number of genes to add must be strictly positive")

        dna_length = len(self.dna)
        if dna_length >= 2:
            offset = self.dna[-1] - self.dna[-2]
        elif dna_length >= 1:
            offset = self.dna[-1]
        else:
            offset = Player.NEW_GENE_DEFAULT_OFFSET

        for index in range(number_of_genes_to_add):
            reference = self.dna[-1] if self.dna else 0
            variation = randint(Player.NEW_GENE_MIN_VARIATION, Player.NEW_GENE_MAX_VARIATION)
            new_value = max(0, reference + offset + variation)
            self.dna.append(new_value)

    @staticmethod
    def __reproduce_dna(first_parent_dna, second_parent_dna):
        if len(first_parent_dna) is not len(second_parent_dna):
            raise ValueError("Player should have the same dna length")

        dna_length = len(first_parent_dna)
        child_dna = []
        for index in range(dna_length):
            if choice([True, False]):
                parent_dna = first_parent_dna
            else:
                parent_dna = second_parent_dna
            child_reference = child_dna[-1] if child_dna else 0
            parent_delta = parent_dna[index] - parent_dna[index - 1] if index > 0 else parent_dna[index]
            child_dna.append(child_reference + parent_delta)
        return child_dna
