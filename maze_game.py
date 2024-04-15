# When a player enters the maze, they choose their name, race, and role, which defines their power/health
## Races to choose from: human, dwarf, elf
## Roles to choose from: wizard, archer, warrior
## Stats max out at 10, if health reaches 0, you must restart
## Must defeat 5 monsters along the way through 5 stages
import random
class Player:
    def __init__(self, name, race, role):
        self.name = name
        self.race = race
        self.role = role
        self.health = 0
        self.power = 0
        self.speed = 0
        self.wisdom = 0
        self.stage = 0
    
        if race == 'human':
            self.health += 6
            self.power = 4
            self.speed = 5
            self.wisdom = 5
        elif race == 'dwarf':
            self.health += 7
            self.power = 6
            self.speed = 4
            self.wisdom = 3
        elif race == 'elf':
            self.health += 4
            self.power = 3
            self.speed = 7
            self.wisdom = 6
        else:
            self.health += 1
            self.power = 1
            self.speed = 1
            self.wisdom = 1
        
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
        else:
            self.power += 1
            self.speed += 1
            self.wisdom += 1

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