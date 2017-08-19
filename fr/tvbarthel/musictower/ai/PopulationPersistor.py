from Player import Player
from Population import Population


class PopulationPersistor:
    GENERATION_FILE_NAME = "generation"

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def load_population(self, path):
        """Load a population from a file.

        :param path: the path of the file
        :return: A Population
        """
        input_file = open(path)
        generation = int(input_file.readline())
        # simply consume the average score
        # noinspection PyUnusedLocal
        average_score = input_file.readline()
        players = []
        for player_line in input_file:
            str_dna = player_line.split(' ')
            dna = [int(a) for a in str_dna]
            players.append(Player(dna))
        input_file.close()

        return Population(players, generation)

    # noinspection PyMethodMayBeStatic
    def save_population(self, population, path):
        """Save a population to a file.

        :param population: the population to save.
        :param path: the path of the folder for the output file.
        """
        fileName = path + self.GENERATION_FILE_NAME + str(population.generation)
        output_file = open(fileName, "w+")
        output_file.write(str(population.get_generation()) + '\n')
        output_file.write(str(population.get_average_score()) + '\n')
        players = population.get_players()
        for player in players:
            str_dna = [str(a) for a in player.get_dna()]
            output_file.write(' '.join(str_dna) + '\n')
        output_file.close()
