class Population:
    def __init__(self, players, generation):
        self.players = players
        self.generation = generation

    def get_players(self):
        return self.players

    def get_generation(self):
        return self.generation
