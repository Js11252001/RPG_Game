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

class MagicCharacter(Character):
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.mana = intelligence * 30 + 50
    
    def printHitpointsAndMana(self):
        print("hitpoints:", self.hitpoints, "mana:", self.mana)
