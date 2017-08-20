from random import choice, random, gauss


class Player:
    MUTATION_FACTORS = [-30, -20, -10, 10, 20, 30]
    NEW_GENE_DEFAULT_DELTA = 800
    NEW_GENE_MAX_VARIATION_NARROW = 50
    NEW_GENE_MAX_VARIATION_BROAD = 500

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
        first_parent_last_meaningful_gene_index = self.score - 1
        second_parent_dna = player.get_dna()
        second_parent_last_meaningful_gene_index = player.score - 1

        if len(first_parent_dna) is not len(second_parent_dna):
            raise ValueError("Player should have the same dna length")

        dna_length = len(first_parent_dna)
        child_dna = []
        parent_pool_dna = [first_parent_dna, second_parent_dna]

        for index in range(dna_length):
            if (index <= first_parent_last_meaningful_gene_index) and \
                    (index <= second_parent_last_meaningful_gene_index):
                parent_dna = choice(parent_pool_dna)
            elif index <= first_parent_last_meaningful_gene_index:
                parent_dna = first_parent_dna
            elif index <= second_parent_last_meaningful_gene_index:
                parent_dna = second_parent_dna
            else:
                parent_dna = None

            if parent_dna:
                child_reference = child_dna[-1] if child_dna else 0
                parent_delta = parent_dna[index] - parent_dna[index - 1] if index > 0 else parent_dna[index]
                gene_value = child_reference + parent_delta
            else:
                reference = child_dna[-1] if child_dna else 0
                last_delta = Player.__get_last_delta(child_dna)
                # Use a broader window to try to find the new rhythm
                gene_value = Player.__get_new_gene_value(reference, last_delta, Player.NEW_GENE_MAX_VARIATION_BROAD)

            child_dna.append(gene_value)

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

        last_delta = Player.__get_last_delta(self.dna)
        for index in range(number_of_genes_to_add):
            reference = self.dna[-1] if self.dna else 0
            # Use a narrow window: try to stay in rhythm at first
            new_value = Player.__get_new_gene_value(reference, last_delta, Player.NEW_GENE_MAX_VARIATION_NARROW)
            self.dna.append(new_value)

    @staticmethod
    def __get_last_delta(dna):
        dna_length = len(dna)
        if dna_length >= 2:
            return dna[-1] - dna[-2]
        elif dna_length >= 1:
            return dna[-1]
        else:
            return Player.NEW_GENE_DEFAULT_DELTA

    @staticmethod
    def __get_new_gene_value(previous_gene, previous_delta, max_variation):
        target_min = max(previous_gene + 200, previous_gene + previous_delta - max_variation)
        target_max = min(previous_gene + 1400, previous_gene + previous_delta + max_variation)
        variation = max(0, min(2, 1 + gauss(0, 0.2))) / 2
        return int(target_min + (target_max - target_min) * variation)
