from random import choice, random, randint


class Player:
    MUTATION_FACTORS = [-30, -20, -10, 10, 20, 30]
    NEW_GENE_DEFAULT_OFFSET = 1000
    NEW_GENE_MIN_VARIATION = -100
    NEW_GENE_MAX_VARIATION = 100

    def __init__(self, dna):
        self.dna = dna
        self.score = 0

    def __str__(self):
        return "Score : " + str(self.score) + " " + str(self.get_deltas())

    def get_score(self):
        return self.score

    def get_dna(self):
        return self.dna

    def get_deltas(self):
        deltas = []
        for index in range(len(self.dna)):
            new_delta = self.dna[index] - self.dna[index - 1] if index > 0 else self.dna[index]
            deltas.append(new_delta)
        return deltas

    def reproduce(self, player):
        """
        Reproduce this player with another player.

        Note: no mutations occurs during the reproduction.
        See mutate().

        :param player: a player.
        :return: a newly created player.
        """
        first_parent_dna = self.get_dna()
        first_parent_score = self.score
        second_parent_dna = player.get_dna()
        second_parent_score = player.score

        if len(first_parent_dna) is not len(second_parent_dna):
            raise ValueError("Player should have the same dna length")

        dna_length = len(first_parent_dna)
        child_dna = []
        parent_pool_dna = [first_parent_dna, second_parent_dna]

        for index in range(dna_length):
            if (index <= first_parent_score) and (index <= second_parent_score):
                parent_dna = choice(parent_pool_dna)
            elif index <= first_parent_score:
                parent_dna = first_parent_dna
            elif index <= second_parent_score:
                parent_dna = second_parent_dna
            else:
                parent_dna = choice(parent_pool_dna)

            child_reference = child_dna[-1] if child_dna else 0
            parent_delta = parent_dna[index] - parent_dna[index - 1] if index > 0 else parent_dna[index]
            child_dna.append(child_reference + parent_delta)

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
