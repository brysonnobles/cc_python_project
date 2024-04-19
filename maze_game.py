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
        self.race = race
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
        self.role = role
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
        self.species = str(random.choices(species_list, weights = species_weights, k = 1))
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
        self.stages = {1: [], 2: [], 3:[], 4:[], 5:[]}
        stages = self.stages
        for value in stages.values():
            number = random.randint(2,5)
            while number > 0:
                try: 
                    value.append(number)
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
Human [Health: 6, Power: 4, Speed: 5, Wisdom: 5]
Dwarf [Health: 7, Power: 6, Speed: 4, Wisdom: 3]
Elf [Health: 4, Power: 3, Speed: 7, Wisdom: 6]'''
role_info = '''
There are three role options:
Wizard [Power: +1, Speed: +2, Wisdom: +3]
Archer [Power: +2, Speed: +3, Wisdom: +1]
Warrior [Power: +3, Speed: +1, Wisdom: +2]'''
print(stat_info)
print(race_info)
print(role_info)
print("-----")

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
maze = Maze()

# Ask for input to enter into stage one
# MAKE THIS PROCESS INTO A FOR LOOP FOR EACH OF THE FIVE STAGES
stats = f"Health: {player.health} / Power: {player.power} / Speed: {player.speed} / Wisdom: {player.wisdom}"
print(f"Welcome to the Maze of Monsters, {player.name}! You have chosen to be a {player.race} {player.role}. Your current stats are: {stats}")
enter = input("To enter the first stage of the Maze of Monsters, please type 'Enter' ")
while enter != 'Enter':
    enter = input("Please type 'Enter' to begin the journey into stage one of the maze. ")
player.stage = 1
next_stage = 0

for stage, paths in maze.stages.items():
    stats = f"Health: {player.health} / Power: {player.power} / Speed: {player.speed} / Wisdom: {player.wisdom}"
    print(maze.stages)
    if player.stage > len(maze.stages):
        print("You have successfully completed the Maze of Monsters! Go to bed...")
    elif player.health == 0:
        print("Unfortunately, you've been slain in the Maze of Monsters. Try again another day!")
    elif next_stage > player.stage: 
        player.stage = next_stage
        print(f"You've made it to stage {player.stage} and your current stats are: {stats}.")
    else:
        while next_stage > player.stage:
            player.stage = next_stage
            print(f"You've made it to stage {player.stage} and your current stats are: {stats}.")
        
            paths = maze.display_paths(player.stage)
            # Prompt for stage path splits
            path_choice = int(input(f"You have stumbled upon a split in the maze. You must choose one of the following paths: {paths} "))
            while path_choice in paths == 'False' and path_choice != 0:
                path_choice = input("Looks like you've tried to go down an imaginary path. Please choose an option from the provided paths above. ")
            paths.pop(paths.index(path_choice))

            # Monster encounter after choosing a path
            monster = Monster(player.stage)
            if monster.species == "empty":
                print("Wow! You found a clear path and can move ahead to the next stage easy peasy.")
                player.health += 1
                player.stage += 1
            else:
                action = input(f"Oh my, you've encountered a {monster.species} [H: {monster.health} / P: {monster.power} / S: {monster.speed} / W: {monster.wisdom}! Will you 'fight' or 'run'? ")
                while action != 'fight' and action != 'run':
                    action = input("Please choose a valid option. Type 'fight' or 'run' to proceed. ")
                if action == 'fight':
                    next_stage = player.stage + 1
                    if player.power > monster.power:
                        print("Congratulations! You have defeated the monster and entered the next stage. You are rewarded with 2 upgrade points.")
                        up_stats = 2
                        while up_stats > 0:
                            try:
                                power_choice = int(input("How many points would you like to assign to power? "))
                                while power_choice > 0 and power_choice < up_stats:
                                    up_stats -= power_choice
                                    player.power += power_choice
                                    if up_stats == 0:
                                        break
                                speed_choice = int(input("How many points would you like to assign to speed? "))
                                if speed_choice > 0:
                                    up_stats -= speed_choice
                                    player.speed += speed_choice
                                    if up_stats == 0:
                                        break
                                wisdom_choice = int(input("How many points would you like to assign to wisdom? "))
                                if wisdom_choice > 0:
                                    up_stats -= wisdom_choice
                                    player.wisdom += wisdom_choice
                                    if up_stats == 0:
                                        break
                            except:
                                print("You have used your upgrade points")
                    elif player.wisdom > monster.wisdom:
                        print(f"Whew! You defeated the monster, but were injured. You've lost {round(monster.power/2)} health, but have entered the next stage and are rewarded with 2 upgrade points.")
                        player.health -= round(monster.power/2)
                        up_stats = 2
                        while up_stats > 0:
                            power_choice = input("How many points would you like to assign to power? ")
                            if power_choice > 0:
                                up_stats -= power_choice
                                player.power += power_choice
                            speed_choice = input("How many points would you like to assign to speed? ")
                            if speed_choice > 0:
                                up_stats -= speed_choice
                                player.speed += speed_choice
                            wisdom_choice = input("How many points would you like to assign to wisdom? ")
                            if wisdom_choice > 0:
                                up_stats -= wisdom_choice
                                player.wisdom += wisdom_choice
                    else:
                        print("Oof, looks like you don't have the power or wisdom to defeat the monster.")
                        player.health = 0
                else:
                    if player.stage == 1:
                        next_stage = player.stage
                        if len(paths) != 0:
                            if player.speed > monster.speed:
                                print("You escaped to the previous stage! You'll need to choose a new path.")
                            elif player.wisdom > monster.wisdom:
                                print(f"You narrowly escaped to the previous stage, but lost {round(monster.power/2)} health in the process.")
                                player.health -= round(monster.power/2)
                            else:
                                print(f"Somehow you escaped, but the monster did some damage and you lost {monster.power} health.")
                                player.health -= monster.power
                        else:
                            print("You coward! Go home...")
                            break
                    else:
                        next_stage = player.stage - 1
                        if player.speed > monster.speed:
                            print("You escaped to the previous stage! You'll need to choose a new path.")
                        elif player.wisdom > monster.wisdom:
                            print(f"You narrowly escaped to the previous stage, but lost {round(monster.power/2)} health in the process.")
                            player.health -= round(monster.power/2)
                        else:
                            print(f"Somehow you escaped, but the monster did some damage and you lost {monster.power} health.")
                            player.health -= monster.power
                            