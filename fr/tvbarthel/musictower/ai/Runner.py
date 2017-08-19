from DeviceBot import DeviceBot
from PopulationPersistor import PopulationPersistor


class Runner:
    """
    Runner used to encapsulate a complete simulation.
    """

    def __init__(self):
        self.bot = DeviceBot()
        self.persistor = PopulationPersistor()
        pass

    def run_simulation(self, input, output):
        """
        Run a complete simulation
        :param input: path of the file for the first generation
        :param output: path for storing each generation
        :return: nothing.
        """
        # load first generation
        population = self.persistor.load_population(input)

        while True:
            print "new generation =============>"
            # play every players
            players = population.get_players()
            for player in players:
                player.score = self.bot.play(player.dna)
                print str(player)

            # store current population
            print "Generation " + str(population)
            self.persistor.save_population(population, output)

            # move on to the next generation
            population = population.next_generation()

            print "new generation <=============="
