import random

keys = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

dict = { }

for i in keys:
    dict[i] = random.randrange(1,21)

for x, y in dict.items():
    print(x, ":", y)