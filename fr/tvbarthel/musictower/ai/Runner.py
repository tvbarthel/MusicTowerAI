from Bot import Bot

print "MusicTower AI"

bot = Bot()
score = bot.play([1000, 1900, 2700, 3600, 4400, 5300, 6200, 7100, 8000, 8900])
print "Game result: " + str(score)
