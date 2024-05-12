import random
import math

class Player:
    def __init__(self, name, race, role):
        self.name = name
        self.race = race
        self.role = role
        self.maxh = 10
        self.maxp = 10
        self.maxs = 10
        self.maxw = 10
        self.stage = 0
        if race == 'Human':
            self.health = 5
            self.power = 3
            self.speed = 4
            self.wisdom = 4
        elif race == 'Dwarf':
            self.health = 6
            self.power = 4
            self.speed = 2
            self.wisdom = 2
        elif race == 'Elf':
            self.health = 4
            self.power = 2
            self.speed = 5
            self.wisdom = 5
        if role == 'Wizard':
            self.power += 1
            self.speed += 1
            self.wisdom += 2
        elif role == 'Archer':
            self.power += 1
            self.speed += 2
            self.wisdom += 1
        elif role == 'Warrior':
            self.power += 2
            self.speed += 1
            self.wisdom += 1

    def upgrade(self, stat, value):
        if stat == "Power":
            self.power += value
        elif stat == "Speed":
            self.speed += value
        elif stat == "Wisdom":
            self.wisdom += value

class Monster:
    def __init__(self, stage):
        self.species = str(random.choices(species_list, weights = species_weights, k = 1))
        if self.species == "empty":
            self.health = 0
            self.power = 0
            self.speed = 0
            self.wisdom = 0
        else:
            self.health = random.randint(1+stage, 4+stage)
            self.power = random.randint(1+stage, 4+stage)
            self.speed = random.randint(1+stage, 4+stage)
            self.wisdom = random.randint(1+stage, 4+stage)

class Maze:
    def __init__(self):
        self.stages = {1: [], 2: [], 3:[], 4:[], 5:[]}
        stages = self.stages
        for value in stages.values():
            number = random.randint(2,5)
            while number > 0:
                try: 
                    value.append(str(number))
                    number -= 1
                except:
                    print("the maze is complete")

    def display_paths(self, player_stage):
        stages = self.stages
        return(stages[player_stage])


species = {"empty": 5, "rat": 10, "wolf": 25, "zombie": 25, "bear": 25, "dragon": 10}
species_list = []
for kind in species.keys():
    species_list.append(kind)
species_weights = []
for weight in species.values():
    species_weights.append(weight)

# Display all info to get started
stat_info = '''
You have four unique stats to track along your journey:
Health [0-10]
Power [0-10]
Speed [0-10]
Wisdom [0-10]'''
race_info = '''
There are three race options:
Human [Health: 5, Power: 3, Speed: 4, Wisdom: 4]
Dwarf [Health: 6, Power: 4, Speed: 2, Wisdom: 2]
Elf [Health: 4, Power: 2, Speed: 5, Wisdom: 5]'''
role_info = '''
There are three role options:
Wizard [Power: +1, Speed: +1, Wisdom: +2]
Archer [Power: +1, Speed: +2, Wisdom: +1]
Warrior [Power: +2, Speed: +1, Wisdom: +1]'''
print(stat_info)
print(race_info)
print(role_info)
print("-----")

# Ask for race input
player_race = input("Choose your race: ")
while player_race != 'Human' and player_race != 'Dwarf' and player_race != 'Elf':
    player_race = input("Oops! You didn't choose a valid option. Please choose Human, Dwarf, or Elf. ")

# Ask for role input
player_role = input("Choose your role: ")
while player_role != 'Wizard' and player_role != 'Archer' and player_role != 'Warrior':
    player_role = input("Oops! You didn't choose a valid option. Please choose Wizard, Archer, or Warrior. ")

# Ask for name input
player_name = input("Choose your name: ")

# Initialize the Player & The Maze
player = Player(player_name, player_race, player_role)
# player.assign_race(player_race)
# player.assign_role(player_role)
player.stage = 0
next_stage = 1
options = 1
maze = Maze()

#• Ask for input to enter into stage one
stats = f"Health: {player.health} / Power: {player.power} / Speed: {player.speed} / Wisdom: {player.wisdom}"
print(f"Welcome to the Maze of Monsters, {player.name} the {player.race} {player.role}! Your current stats are: {stats}")
enter = input("To enter the first stage of the Maze of Monsters, please type 'Enter' ")
while enter != 'Enter':
    enter = input("Please type 'Enter' to begin the journey into stage one of the maze. ")
print("-----")
player.stage += 1
#• Looping through each of the 5 stages of the maze
if player.stage > len(maze.stages):
        print("You have successfully completed the Maze of Monsters! Go to bed...")
else:
    for stage, paths in maze.stages.items():
        if player.health == 0:
            print("Unfortunately, you've been slain in the Maze of Monsters. Try again another day!")
        elif options == 0: 
            print("You coward! Go home...")
            break
        else:
            stats = f"Health: {player.health} / Power: {player.power} / Speed: {player.speed} / Wisdom: {player.wisdom}"
            # player.stage = next_stage
            print(f"You've made it to stage {player.stage} and your current stats are: {stats}.")
            print("~~~~~")
            paths = maze.display_paths(player.stage)
            #• Prompt for stage path splits
            path_choice = input(f"You have stumbled upon a split in the maze. You must choose one of the following paths: {paths} ") 
            while path_choice not in paths:
                path_choice = input("Looks like you've tried to go down an imaginary path. Please choose an option from the provided paths above. ")
            # next_stage += 1
            paths.pop(paths.index(path_choice))
            options = len(paths)

            #• Monster encounter after choosing a path
            monster = Monster(player.stage)
            if str(monster.species) == "empty":
                print("Wow! You found a clear path and can move ahead to the next stage easy peasy. *Gain 1 Health*")
                player.health += 1
            else:
                action = input(f"Oh my, you've encountered a {monster.species} [H: {monster.health} / P: {monster.power} / S: {monster.speed} / W: {monster.wisdom}]! Will you 'fight' or 'run'? ")
                while action != 'fight' and action != 'run':
                    action = input("Please choose a valid option. Type 'fight' or 'run' to proceed. ")
                if action == 'fight':
                    if (player.power > monster.power and player.wisdom < monster.wisdom) or (player.power == monster.power and player.wisdom > monster.wisdom):
                        health_loss = math.ceil(0.25*monster.power)
                    elif (player.power == monster.power and player.wisdom == monster.wisdom) or (player.power < monster.power and player.wisdom > monster.wisdom):
                        health_loss = math.ceil(0.50*monster.power)
                    elif (player.power == monster.power and player.wisdom < monster.wisdom) or (player.power < monster.power and player.wisdom == monster.wisdom):
                        health_loss = math.ceil(0.75*monster.power)
                        # up_stats = 2
                        # while up_stats > 0:
                        #     for stat in ["Power","Speed","Wisdom"]:
                        #         if up_stats == 0:
                        #             break
                        #         else:
                        #             try:
                        #                 upgrade = int(input(f"Upgrade {stat} [{up_stats} left] "))
                        #                 while upgrade > up_stats or upgrade < 0:
                        #                     upgrade = int(input(f"You don't have that many upgrades. Upgrade {stat} [{up_stats} left] "))
                        #                 player.upgrade(stat,upgrade)
                        #                 up_stats -= upgrade
                        #             except:
                        #                 print("You have not entered a numerical value.")
                        #                 continue
                    elif player.power < monster.power and player.wisdom < monster.wisdom:
                        print("Oof, looks like you don't have the power or wisdom to defeat the monster.")
                        player.health = 0
                    else:
                        health_loss = 0
                    player.health -= health_loss
                    player.health += 2
                    print(f"Congratulations! You have defeated the monster and taken {health_loss} damage. You are rewarded with 2 upgrades and regenerate 2 health.")
                    up_stats = 2
                    print("***Please choose how you'd like to upgrade your stats:")
                    while up_stats > 0:
                        for stat in ["Power","Speed","Wisdom"]:
                            if up_stats == 0:
                                break
                            else:
                                try:
                                    upgrade = int(input(f"Upgrade {stat} [{up_stats} left] "))
                                    while upgrade > up_stats or upgrade < 0:
                                        upgrade = int(input(f"You don't have that many upgrades. Upgrade {stat} [{up_stats} left] "))
                                    player.upgrade(stat,upgrade)
                                    up_stats -= upgrade
                                except:
                                    print("You have not entered a numerical value.")
                                    continue
                else:
                    if player.stage == 1:
                        if options == 0:
                            break
                        else:
                            player.stage -= 1
                            if player.speed > monster.speed:
                                print("You escaped to the previous stage! You'll need to choose a new path.")
                            elif player.wisdom > monster.wisdom:
                                print(f"You narrowly escaped to the previous stage, but lost {round(monster.power/2)} health in the process.")
                                player.health -= round(monster.power/2)
                            else:
                                print(f"Somehow you escaped, but the monster did some damage and you lost {monster.power} health.")
                                player.health -= monster.power
                    else:
                        player.stage -= 1
                        if options == 0:
                            break
                        else:
                            if player.speed > monster.speed:
                                print("You escaped to the previous stage! You'll need to choose a new path.")
                            elif player.wisdom > monster.wisdom:
                                print(f"You narrowly escaped to the previous stage, but lost {round(monster.power/2)} health in the process.")
                                player.health -= round(monster.power/2)
                            else:
                                print(f"Somehow you escaped, but the monster did some damage and you lost {monster.power} health.")
                                player.health -= monster.power      