RULES (in progress):
> You have four unique stats with a maximum of 10:
>>> Health // This helps you survive throughout the maze
>>> Power // This helps you defeat monsters in the maze
>>> Speed // This helps you run away from powerful monsters
>>> Wisdom // This helps you take less damage when fighting/running

> There are three race options:
>>> Human [Health: 5, Power: 3, Speed: 4, Wisdom: 4]
>>> Dwarf [Health: 6, Power: 4, Speed: 2, Wisdom: 2]
>>> Elf [Health: 4, Power: 2, Speed: 5, Wisdom: 5]

> There are three role options:
>>> Wizard [Power: +1, Speed: +1, Wisdom: +2]
>>> Archer [Power: +1, Speed: +2, Wisdom: +1]
>>> Warrior [Power: +2, Speed: +1, Wisdom: +1]

> Each stage & path has the following options:
>>> When the maze is entered, the entire maze structure is built out in the program
>>> Each stage consists of 2-5 possible paths
>>> Each path will have either a monster guarding it or it will be a clear path
>>>>> Currently, there are 5 different monster types: rat, wolf, zombie, bear, dragon
>>>>> The monster types don't differ in the stats that are provided them, it's solely a name
>>> As you progress through the stages, the monsters get increasingly difficult in the following structure:
>>>>> Health & Power are randomly chosen with the following: 1+n to 4+n where n = current stage
>>>>> Speed & Wisdom are randomly chosen with the following: 2+n to 5+n where n = current stage
>>> If you run away from a monster successfully, you are prompted to go down one of the remaining paths
>>> If there are no paths left in the stage, you are considered a Coward!

GAME FLOW:
1. Choose a name, then a race and role which determines your skills & health
2. Three main skills (power, speed, and wisdom) are calculated and health is established
    a. you should have the ability to check the status of your skills at any point by typing "stats" at any time
4. As the player proceeds through the maze, they choose their path for each stage
    a. most paths will have monsters, but sometimes it may be a clear path
5. When a player encounters a monster, they will have two options (fight, run)
    > FIGHT 
    1. IF: higher power & higher wisdom >> you will defeat the monster and lose 0% health
    2. IF: equal power & higher wisdom OR: lesser power & higher wisdom >> you will defeat, but lose health equal to 25% of the monster's power
    3. IF: equal power & equal wisdom OR: higher power & equal/lesser wisdom >> you will defeat, but lose health equal to 50% of the monster's power
    4. IF: equal power & lesser wisdom OR: lesser power & equal wisdom >> you will defeat, but lose health equal to 75% of the monster's power
    5. IF: lesser power & lesser wisdom >> you will be defeated
    > RUN
    1. IF: higher speed & higher/equal wisdom >> you will defeat the monster and lose 0% health
    2. IF: higher speed & lesser wisdom OR: equal speed & higher wisdom >> you will defeat, but lose health equal to 25% of the monster's power
    3. IF: equal speed & equal wisdom OR: lesser speed & higher wisdom >> you will defeat, but lose health equal to 50% of the monster's power
    4. IF: equal speed & lesser wisdom OR: lesser speed & equal wisdom >> you will defeat, but lose health equal to 75% of the monster's power
    5. IF: lesser speed & lesser wisdom >> you will be defeated
6. When a stage is cleared:
    a. if you kill the monster and lose 0% health, you can upgrade 3 stats and regain 2 health
    b. if you kill a monster, but lose health, you can upgrade 2 stat points and regain 3 health
    c. if you clear a stage through an easy path, you can upgrade 2 stat points and gain 1 health
7. After all 5 stages are completed, the player will exit the maze and complete the game successfully
