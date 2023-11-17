class Char:
    def __init__(self, name, race, classs, strength, constitution, dexterity, intelligence, wisdom, charisma):
        self.name = name
        self.race = race
        self.classs = classs
        self.str = strength
        self.con = constitution
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma

dwarf = Char('Dalgurn', 'Dwarf', 'Warrior', 15, 15, 13, 11, 14, 13)
elf = Char('Torrieth', 'Elf', 'Mage', 7, 10, 13, 15, 15, 16)


print(dwarf.__dict__)
print(elf.__dict__)