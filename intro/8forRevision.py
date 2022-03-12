import random

class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = constitution * 30 + 50
        
    def printStats(self):
        print("strength: ", self.strength)
        print("dexterity: ", self.dexterity)
        print("constitution: ", self.constitution)
        print("intelligence", self.intelligence)
        print("wisdom: ", self.wisdom)
        print("charisma: ", self.charisma)

    def printHitpoints(self):
        print("hitpoints: ", self.hitpoints)

    def attack(self):
        return random.randrange(1, self.strength + 1)

    def defense(self, val):
        t = random.randrange(1, 21)
        if t >= self.dexterity:
            # val - self.attack()
            self.hitpoints -= val
        else:
            # I think not cause dmg is not right
            self.hitpoints -= val/2
    
    def heal(self, val):
        self.hitpoints += val

if __name__ == "__main__":
    c1 = Character(10,9,1,5,7,7)
    c2 = Character(10,8,1,6,3,15)
    while c1.hitpoints > 0 and c2.hitpoints > 0:
        c1.defense(c2.attack())
        c2.defense(c1.attack())
        print("c1:", c1.hitpoints)
        print("c2:", c2.hitpoints)
    if c1.hitpoints < 0:
        print("c1 dead, c2 win")
    else:
        print("c2 dead, c1 win")