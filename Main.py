from fr.tvbarthel.musictower.ai.Runner import Runner

FIRST_GENERATION_PATH = "static/population.txt"
OUTPUT = "static/attemp1/"

print "========= MusicTower AI ========="
runner = Runner()
runner.run_simulation(FIRST_GENERATION_PATH, OUTPUT, 100, 100)
