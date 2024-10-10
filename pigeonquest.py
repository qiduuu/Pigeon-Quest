# for cool typewriter effect on text
# MUST RUN "pip install pywriter" FOR IT TO WORK
import pywriter

#time is important for waiting/sleep commands
import time

#list of commands
commands = "OPEN INVENTORY: inv, inventory\nVIEW STATS: stats\nATTACK: attack, atk, hit, stab\n"

hp = 100
xp = 0
level = 0
dmg = 10

'''
Inventory
-------------------------------------
SLOT 1: 
SLOT 2:
SLOT 3:
'''
slot1 = ""
slot2 = ""
slot3 = ""

inBattle = False
Enemy = ""

hasAtkUp1 = False
hasAtkUp2 = False
hasAtkUp3 = False

# Creates classes for enemies to in the future make multiple instances of the same enemy type 
class Duckling:
    hp = 15
    dmg = 5
    name = "Duckling"
    xpGain = 10
class Swan:
    hp = 25
    dmg = 10
    name = "Swan"
    xpGain = 15
class CanGoose:
    hp = 75
    dmg = 15
    name = "Canadian Goose"
    xpGain = 25
class Dove:
    hp = 50
    dmg = 10
    name = "Dove"
    xpGain = 20
class Puffin:
    hp = 100
    dmg = 20
    name = "Puffin"
    xpGain = 50

# checks if user has upgrades and applies them
def checkUpgrades():
    if hasAtkUp1:
        dmg = 15
    if hasAtkUp2:
        dmg = 25
    if hasAtkUp3:
        dmg = 40

# Checks for user input on commands from the command variable above such as stats and inventory
def checkInputs():
    global hp
    global inBattle
    global dmg
    global level
    global xp

    pywriter.write("\n-------------------------------------\nCOMMAND LIST\n-------------------------------------\n" + commands + "-------------------------------------", rate=0.01)
    userInput = input('\n').lower()
    if userInput == "inv" or userInput.lower() == "inventory":
        pywriter.write("\nInventory\n------------------------------------------\nSLOT 1: " + slot1 + "\nSLOT 2: " + slot2 + "\nSLOT 3: " + slot3 + "\n------------------------------------------", rate=0.01)
        time.sleep(1)
        checkInputs()
    elif userInput == "stats":
        pywriter.write("HP: " + str(hp) + "/100", rate=0.01)
        pywriter.write("LVL: " + str(level), rate=0.01)
        pywriter.write("XP: " + str(xp) + "/100", rate=0.01)
        time.sleep(1)
        checkInputs()
    elif (userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "stab") and inBattle == True:

        pywriter.write("\nYou hit " + Enemy.name + " for " + str(dmg) + " damage!\n", rate=0.01)
        Enemy.hp = Enemy.hp - dmg
        time.sleep(1)
        if Enemy.hp <= 0:
            pywriter.write(Enemy.name + " has been vanquished! Congratulations!\n", rate=0.01)
            pywriter.write("You gained " + str(Enemy.xpGain) + " XP! :)", rate=0.01)
            inBattle = False
        else:
            pywriter.write("\n" + Enemy.name + " is now at " + str(Enemy.hp) + "hp", rate=0.01)
            time.sleep(1)
            pywriter.write("\n" + Enemy.name + " viciously attacks you, dealing " + str(Enemy.dmg) + " damage!", rate=0.01)
            hp = hp - Enemy.dmg 
            checkInputs()
    elif (userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "stab") and inBattle == False:
        pywriter.write("You are not in a battle right now. \n\n", rate=0.01)
    else:
        pywriter.write("Invalid command.\n\n", rate=0.01)
        time.sleep(1)
        checkInputs()



pywriter.write("WARNING: DO NOT PRESS ANYTHING WHILE TEXT IS BEING TYPED AS IT MAY MESS UP AREAS REQUIRING INPUT", rate=0.01)

input("\nType anything to continue: ")
print("\n")

pywriter.write("You are the last pigeon left.\nYour quest is to defeat the Duck Lord.\n\nYour journey begins now.", rate=0.01)

time.sleep(2.5)
username = input("\nName your pigeon adventurer: ")
pywriter.write("\n\nWelcome, " + username + ", to Pigeon Quest.", rate=0.01)

# Battle 1 Start
inBattle = True
bob = Duckling()
Enemy = bob
Enemy.name = "Duckling Bob"
time.sleep(1)
# fight intro message
pywriter.write("\nA little duck jumps out of a nearby bush holding a sword!", rate=0.01)
time.sleep(2)
pywriter.write("\n" + Enemy.name + " challenges you to a duel!", rate=0.01)
time.sleep(1)
pywriter.write("\n\nDUCKLING HP: " + str(bob.hp) + "\n\nYOUR HP: " + str(hp), rate=0.01)


time.sleep(2)
checkInputs()
# Battle 1 End

time.sleep(1)
pywriter.write("\n-------------------------------------", rate=0.01)

pywriter.write("\nYou see a village out to the north and begin heading towards it.", rate=0.01)
pywriter.write("...", rate=0.5)
pywriter.write("As you approach the village, you notice someone trying to get your attention.", rate=0.01)
pywriter.write("It's another pigeon! You believed you were the last of your kind, \nhowever this old pigeon man is proof there could be more of you out there!", rate=0.01)
time.sleep(1.5)
input("\nType anything to continue: ")
print("\n")
pywriter.write("He speaks in a slow, raspy voice\n", rate=0.03)
pywriter.write("> Old Man Pigeon: Hello, little pigeon.", rate=0.1)
pywriter.write("> Old Man Pigeon: I've been out that adventurin' business a long long time, boy, \nso I reckon this one's for you", rate=0.1)
time.sleep(0.5)
pywriter.write("He hands you an old, torn piece of paper from a quest board.", rate=0.02)
time.sleep(1)
print("----------------------------------------------------------------------------------\nADVENTURER REQUIRED!!!!!!\n\nTHE DUCK LORD HAS BECOME TO POWERFUL,\nSOMEBODY MUST DEFEAT HIM!!!")
time.sleep(0.75)
input("\nType anything to continue: ")
print("\n")
pywriter.write("\n\nREWARD: Honor and Glory!", rate=0.05)
pywriter.write("\n...", rate=0.175)
pywriter.write("\n...", rate=0.175)
pywriter.write("\nand 9 trillion shmillion pigeon dollars", rate=0.03)
print("----------------------------------------------------------------------------------")

takeQuest = input("\nDo you accept this quest? ('yes' or 'no') ").lower()

if takeQuest != "yes":
    print("You change your mind and decide to take the quest anyway.")
