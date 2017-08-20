from LocalBot import LocalBot
from PopulationPersistor import PopulationPersistor


class Runner:
    """
    Runner used to encapsulate a complete simulation.
    """

    def __init__(self):
        self.bot = LocalBot()
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
            population = self.proceed_to_next_generation(output, population)

    def run_simulation(self, input, output, count, times):
        """
               Run a complete simulation
               :param input: path of the file for the first generation
               :param output: path for storing each generation
               :param count: number max of generation
               :param times: number of times the simulation must be launched
               :return: nothing.
               """
        average_generation = 0
        for j in range(times):
            population = self.persistor.load_population(input)
            successful_generation = count
            for i in range(count):
                try:
                    population = self.proceed_to_next_generation(output, population)
                except ValueError:
                    successful_generation = i
                    break
            average_generation += successful_generation
        print "Average: " + str(average_generation / times)

    def proceed_to_next_generation(self, output, population):
        """
        Make the current generation live and reproduce to give birth to the next generation.
        :param output: output where to store given generation once lived.
        :param population: current generation.
        :return: new generation born from the current one.
        """
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
        print "new generation <=============="
        return population.next_generation()
