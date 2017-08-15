from fr.tvbarthel.musictower.ai.Player import Player
from fr.tvbarthel.musictower.ai.Population import Population


class PopulationPersistor:
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def load_population(self, path):
        with open(path) as input_file:
            generation = int(input_file.readline())
            # simply consume the average score
            # noinspection PyUnusedLocal
            average_score = input_file.readline()
            players = []
            for player_line in input_file:
                str_dna = player_line.split(' ')
                dna = [int(a) for a in str_dna]
                players.append(Player(dna))

            return Population(players, generation)

    # noinspection PyMethodMayBeStatic
    def save_population(self, population, path):
        with open(path, "w+") as output_file:
            output_file.write(str(population.get_generation()) + '\n')
            output_file.write(str(population.get_average_score()) + '\n')
            players = population.get_players()
            for player in players:
                str_dna = [str(a) for a in player.get_dna()]
                output_file.write(' '.join(str_dna) + '\n')
