from LocalBot import LocalBot
from PopulationPersistor import PopulationPersistor


class SimulationStats:
    """
    Used to encapsulate stats linked to a simulation.
    """

    def __init__(self, generation, average_score, max_score):
        """
        Used to encapsulate stats linked to a simulation.
        :param generation: last generation reached
        :param average_score: averaged score of players of the last generation
        :param max_score: max score reached by a player in the last generation
        """
        self.gen = generation
        self.avg_score = average_score
        self.max_score = max_score

    def __str__(self):
        return "Generation: " + str(self.gen) + " score " + str(self.avg_score) + " max score " + str(self.max_score)


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
        average_score = 0
        simulation_stats = []
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
            simulation_stats.append(
                SimulationStats(successful_generation, self.last_average_score, self.last_max_score))
            average_score += self.last_average_score

        # log some stats on the simulations performed
        simulation_stats.sort(key=lambda stat: stat.max_score)
        for stats in simulation_stats:
            print "\t" + str(stats)

        print "Average generation: " + str(average_generation / times) + " for score " + str(average_score / times)

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

        # store data for stats
        self.last_max_score = population.get_max_score()
        self.last_average_score = population.get_average_score()

        # move on to the next generation
        print "new generation <=============="
        return population.next_generation()
