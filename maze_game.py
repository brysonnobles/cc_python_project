# When a player enters the maze, they choose their name, race, and role, which defines their power/health
## Races to choose from: human, dwarf, elf
## Roles to choose from: wizard, archer, warrior
## Stats max out at 10, if health reaches 0, you must restart
## Must defeat 5 monsters along the way through 5 stages
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.race = ""
        self.role = ""
        self.health = 0
        self.power = 0
        self.speed = 0
        self.wisdom = 0
        self.stage = 0
    
    def assign_race(self, race):
        if race == 'human':
            self.health += 6
            self.power += 4
            self.speed += 5
            self.wisdom += 5
        elif race == 'dwarf':
            self.health += 7
            self.power += 6
            self.speed += 4
            self.wisdom += 3
        elif race == 'elf':
            self.health += 4
            self.power += 3
            self.speed += 7
            self.wisdom += 6
    
    def assign_role(self, role)
        if role == 'wizard':
            self.power += 1
            self.speed += 2
            self.wisdom += 3
        elif role == 'archer':
            self.power += 2
            self.speed += 3
            self.wisdom += 1
        elif role == 'warrior':
            self.power += 3
            self.speed += 1
            self.wisdom += 2

# When a player encounters a monster, it's chosen at random depending on how far they are in the maze
## There are stronger monsters along the way, but defeating them upgrades your player
class Monster:
    def __init__(self):
        self.species = ""
        self.health = 0
        self.power = 0
        self.speed = 0
        self.wisdom = 0
    
    def assign_power(self, stage):
        self.health = random.randint(0+stage, 3+stage)
        self.power = random.randint(0+stage, 3+stage)
        self.speed = random.randint(0+stage, 3+stage)
        self.wisdom = random.randint(0+stage, 3+stage)

# def species

class Maze:
    def __init__(self):
        self.stages = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    def assign_paths(self):
        stages = self.stages
        for stage in stages.keys:
            stage.value = random.randint(2,5)

stat_info = '''
You have four unique stats to track along your journey:
Health [0-10]
Power [0-10]
Speed [0-10]
Wisdom [0-10]
'''
race_info = '''
There are three race options:
Human [Health: 6, Power: 4, Speed: 5, Wisdom: 5]
Dwarf [Health: 7, Power: 6, Speed: 4, Wisdom: 3]
Elf [Health: 4, Power: 3, Speed: 7, Wisdom: 6]
'''
role_info = '''
There are three role options:
Wizard [Power: +1, Speed: +2, Wisdom: +3]
Archer [Power: +2, Speed: +3, Wisdom: +1]
Warrior [Power: +3, Speed: +1, Wisdom: +2]
'''
print(stat_info)
print(race_info)
print(role_info)
player_race = input("Please choose your race to determine your starting levels for the Maze.")
while player_race != 'Human' or player_race != 'Dwarf' or player_race != 'Elf':
    player_race = input("Oops! You didn't choose a valid option. Please choose Human, Dwarf, or Elf.")
player_role = input("Please choose your role to determine your additional stats.")
while player_role != 'Wizard' or player_race != 'Arhcer' or player_race != 'Warrior':
    player_race = input("Oops! You didn't choose a valid option. Please choose Wizard, Archer, or Warrior.")
player_name = input("You have stumbled upon the Maze of Monsters. Please provide your adventurer's name before proceeding into the Maze. ")
