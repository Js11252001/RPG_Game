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
        Character.__init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.mana = intelligence * 30 + 50
    
    def printHitpointsAndMana(self):
        print("hitpoints:", self.hitpoints, "mana:", self.mana)

    def magicMissile(self):
        self.mana -= 5
        return random.randrange(5, 11)

    def fireball(self):
        self.mana -= 10
        return random.randrange(10, 21)
    
    def healMana(self, val):
        self.mana += val
    
if __name__ == "__main__":
    c1 = Character(12,13,9,10,7,10)
    c1.printHitpoints()
    c1.printStats()
    c1.attack()
    c1.defense(10)
    c1.heal(3)
    print("___________________")
    c1.printHitpoints()
    c1.printStats()
    print("___________________")
    m1 = MagicCharacter(10,2,4,1,10,5)
    m1.printHitpointsAndMana()
    c1.defense(m1.magicMissile())
    m1.printHitpointsAndMana()
    m1.healMana(5)
    m1.printHitpointsAndMana()
    c1.printHitpoints()
    c1.defense(m1.fireball())
    c1.printHitpoints()
    m1.printHitpointsAndMana()
