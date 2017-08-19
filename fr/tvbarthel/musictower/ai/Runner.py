from PopulationPersistor import PopulationPersistor

print "MusicTower AI"

# load population
persistor = PopulationPersistor()
popupation = persistor.load_population("static/fake_population.txt")

# fake result
for player in popupation.players:
    player.score = 5

# next gen
nextPopulation = popupation.next_generation()

print str(popupation)
print str(nextPopulation)
