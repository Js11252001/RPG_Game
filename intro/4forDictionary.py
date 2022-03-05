import random
characterdict = {
    "strength": 10, 
    "dexterity" : 3, 
    "constitution" : 4, 
    "intelligence" : 14, 
    "wisdom" : 13, 
    "charisma" : 13
}
print(characterdict)
# for loop
for x, y in characterdict.items():
  print(x, y)

print("-----------test-----------")
# test strength
if "strength" in characterdict:
    print(characterdict["strength"])
else:
    print("strength isn't a character stat.")

# test speed
if "speed" in characterdict:
    print(characterdict["speed"])
else:
    print("speed isn't a character stat.")