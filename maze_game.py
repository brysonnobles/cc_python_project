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
        if race == 'Human':
            self.health += 6
            self.power += 4
            self.speed += 5
            self.wisdom += 5
        elif race == 'Dwarf':
            self.health += 7
            self.power += 6
            self.speed += 4
            self.wisdom += 3
        elif race == 'Elf':
            self.health += 4
            self.power += 3
            self.speed += 7
            self.wisdom += 6
    
    def assign_role(self, role):
        if role == 'Wizard':
            self.power += 1
            self.speed += 2
            self.wisdom += 3
        elif role == 'Archer':
            self.power += 2
            self.speed += 3
            self.wisdom += 1
        elif role == 'Warrior':
            self.power += 3
            self.speed += 1
            self.wisdom += 2

class Monster:
    def __init__(self, stage):
        self.species = random.choices(species_list)
        if self.species == "empty":
            self.health = 0
            self.power = 0
            self.speed = 0
            self.wisdom = 0
        else:
            self.health = random.randint(0+stage, 3+stage)
            self.power = random.randint(0+stage, 3+stage)
            self.speed = random.randint(0+stage, 3+stage)
            self.wisdom = random.randint(0+stage, 3+stage)

class Maze:
    def __init__(self):
        self.stages = [1,2,3,4,5]
        self.paths = { stage: random.randint(2,5) for stage in self.stages }

    # def assign_paths(self):
    #     stages = { stage: random.randint(2,5) for stage in self.stages }
    #     return(stages)


species_list = {"empty": 5, "rat": 10, "wolf": 25, "zombie": 25, "bear": 25, "dragon": 10}

stat_info = '''
You have four unique stats to track along your journey:
Health [0-10]
Power [0-10]
Speed [0-10]
Wisdom [0-10]'''
race_info = '''
There are three race options:
Human [Health: 6, Power: 4, Speed: 5, Wisdom: 5]
Dwarf [Health: 7, Power: 6, Speed: 4, Wisdom: 3]
Elf [Health: 4, Power: 3, Speed: 7, Wisdom: 6]'''
role_info = '''
There are three role options:
Wizard [Power: +1, Speed: +2, Wisdom: +3]
Archer [Power: +2, Speed: +3, Wisdom: +1]
Warrior [Power: +3, Speed: +1, Wisdom: +2]'''
## Display all info to get started
print(stat_info)
print(race_info)
print(role_info)

# Ask for race input
player_race = input("Please choose your race to determine your starting levels for the Maze. ")
while player_race != 'Human' and player_race != 'Dwarf' and player_race != 'Elf':
    player_race = input("Oops! You didn't choose a valid option. Please choose Human, Dwarf, or Elf. ")

# Ask for role input
player_role = input("Please choose your role to determine your additional stats. ")
while player_role != 'Wizard' and player_role != 'Archer' and player_role != 'Warrior':
    player_role = input("Oops! You didn't choose a valid option. Please choose Wizard, Archer, or Warrior. ")

# Ask for name input
player_name = input("You have made it to the Maze of Monsters. Please provide your adventurer's name before proceeding into the Maze. ")

# Initialize the Player & The Maze
player = Player(player_name)
player.assign_race(player_race)
player.assign_role(player_role)
stats = f"Health: {player.health} / Power: {player.power} / Speed: {player.speed} / Wisdom: {player.wisdom}"
maze = Maze()
paths = maze.paths

# Ask for input to enter into stage one
# MAKE THIS PROCESS INTO A FOR LOOP FOR EACH OF THE FIVE STAGES
print(f"Welcome to the Maze of Monsters, {player.name}! You have chosen to be a {player.race} {player.role}. Your current stats are {stats}")
stage_one = input("To enter the first stage of the Maze of Monsters, please type 'Enter' ")
while stage_one != 'Enter':
    stage_one = input("Please type 'Enter' to begin the journey into stage one of the maze. ")
player.stage += 1
stage_paths = []
for stage, path in paths.values():
    if stage == player.stage:
        stage_paths.append(path)
path_choice = input(f"You have stumbled upon the first split in the maze. You must choose one of the following paths: {stage_paths} ")
while path_choice not in stage_paths:
    input("Looks like you've tried to go down an imaginary path. Please choose an option from the provided paths above. ")
paths.popitem(player.stage, path_choice)
monster = Monster(player.stage)
if monster.species == "empty":
    print("Wow! You found a clear path and can move ahead to the next stage easy peasy.")
    player.health += 3
else:
    action = input(f"Oh my, you've encountered a {monster.species} [H: {monster.health} / P: {monster.power} / S: {monster.speed} / W: {monster.wisdom}! Will you 'fight' or 'run'?")
    while action != 'fight' and action != 'run':
        action = input("Please choose a valid option. Type 'fight' or 'run' to proceed.")
