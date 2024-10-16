# for cool typewriter effect on text
# MUST RUN "pip install pywriter" FOR IT TO WORK
import pywriter

#time is important for waiting/sleep commands
import time

#list of commands
commands = "OPEN INVENTORY: inv, inventory\nVIEW STATS: stats\nATTACK: peck\nUSE ITEM: use"

hp = 100
xp = 0
level = 1
dmg = 12
dmg2 = 35

'''
Inventory
-------------------------------------
SLOT 1: 
'''
slot1 = ""

inBattle = False
Enemy = ""

hasAtk2 = False
atk2Left = 8

hasHealthPot = False

# Creates classes for enemies to in the future make multiple instances of the same enemy type 
class Duckling:
    hp = 15
    dmg = 5
    name = "Duckling"
    xpGain = 10
class CanGoose:
    hp = 75
    dmg = 15
    name = "Canadian Goose"
    xpGain = 75
class Dove:
    hp = 50
    dmg = 10
    name = "Dove"
    xpGain = 50

#duck lord, easier for managing health and stuff
class DuckLord:
    hp = 120
    dmg = 17.5
    name = "The Duck Lord"
    xpGain = 120

def pressEnter():
    input("\nPress ENTER to continue: ")
    print("\n")


# Checks for user input on commands from the command variable above such as stats and inventory
def checkInputs():
    global hp
    global inBattle
    global dmg
    global level
    global xp
    global commands
    global atk2Left
    global hasAtk2
    global hasHealthPot

    if hasAtk2 == True:
        commands = "OPEN INVENTORY: inv, inventory\nVIEW STATS: stats\nATTACK: peck\nUSE ITEM: use\nATTACK 2: slash" + "(" + str(atk2Left) + " USES LEFT)"

    print("\n-------------------------------------\nCOMMAND LIST\n-------------------------------------\n" + commands + "\n-------------------------------------")
    userInput = input('\n').lower()
    if userInput == "inv" or userInput.lower() == "inventory":
        pywriter.write("\nInventory\n------------------------------------------\nSLOT 1: " + slot1 + "\n------------------------------------------", rate=0.01)
        time.sleep(1)
        checkInputs()
    elif userInput == "stats":
        pywriter.write("HP: " + str(hp) + "/100", rate=0.01)
        pywriter.write("LVL: " + str(level), rate=0.01)
        pywriter.write("XP: " + str(xp) + "/100", rate=0.01)
        time.sleep(1)
        checkInputs()
    elif (userInput == "use") and hasHealthPot == True:
        hp = hp + 50
        time.sleep(1)
        pywriter.write("\n" + Enemy.name + " viciously attacks you, dealing " + str(Enemy.dmg) + " damage!", rate=0.01) # make damage message sorta random
        hp = hp - Enemy.dmg 
        if hp <= 0:
            pywriter.write("\nYOU DIED :(", rate=0.08)
            exit()
        else:
            checkInputs()
    elif (userInput == "peck") and inBattle == True:

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
            pywriter.write("\n" + Enemy.name + " viciously attacks you, dealing " + str(Enemy.dmg) + " damage!", rate=0.01) # make damage message sorta random
            hp = hp - Enemy.dmg 
            if hp <= 0:
                pywriter.write("\nYOU DIED :(", rate=0.08)
                exit()
            else:
                checkInputs()
    elif userInput == "slash" and inBattle == True and hasAtk2 == True:
        atk2Left = atk2Left - 1
        pywriter.write("\nYou hit " + Enemy.name + " for " + str(dmg2) + " damage!\n", rate=0.01)
        Enemy.hp = Enemy.hp - dmg2
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
            if hp <= 0:
                pywriter.write("\nYOU DIED :(", rate=0.08)
                exit()
            else:
                checkInputs()
    elif userInput == "use" and hasHealthPot == False:
        pywriter.write("There is no item in your inventory.\n\n", rate=0.01)
        checkInputs()
    elif (userInput == "peck" or userInput == "slash" or userInput == "use") and inBattle == False:
        pywriter.write("You are not in a battle right now. \n\n", rate=0.01)
        checkInputs()
    else:
        pywriter.write("Invalid command.\n\n", rate=0.01)
        time.sleep(1)
        checkInputs()



pywriter.write("WARNING: DO NOT PRESS ANYTHING WHILE TEXT IS BEING TYPED AS IT MAY MESS UP AREAS REQUIRING INPUT", rate=0.01)

pressEnter()

pywriter.write("You are the last pigeon left.\nYour quest is to defeat the Duck Lord.\n\nYour journey begins now.", rate=0.01)

time.sleep(2.5)
username = input("\nName your pigeon adventurer: ")
pywriter.write("\n\nWelcome, " + username + ", to Pigeon Quest.", rate=0.01)

# Tutorial Battle Start
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
pywriter.write("\n\nDUCKLING HP: " + str(Enemy.hp) + "\n\nYOUR HP: " + str(hp), rate=0.01)


time.sleep(2)
checkInputs()
print("\nLEVEL UP!")
pywriter.write("\nYou are now level 2!", rate=0.03)
level = 2
# Tutorial Battle End

pressEnter()

time.sleep(1)
pywriter.write("\n-------------------------------------", rate=0.01)

pywriter.write("\nYou see a village out to the north and begin heading towards it.", rate=0.01)
pywriter.write("...", rate=0.5)
pywriter.write("As you approach the village, you notice someone trying to get your attention.", rate=0.01)
pywriter.write("It's another pigeon! You believed you were the last of your kind, \nhowever this old pigeon man is proof there could be more of you out there!", rate=0.01)
time.sleep(1.5)
pressEnter()
pywriter.write("He speaks in a slow, raspy voice\n", rate=0.03)
pywriter.write("> Old Man Pigeon: Hello, little pigeon.", rate=0.1)
pywriter.write("> Old Man Pigeon: I've been outta that adventurin' business a long long time, boy, \nso I reckon this one's for you", rate=0.1)
time.sleep(0.5)
pywriter.write("He hands you an old, torn piece of paper from a quest board.", rate=0.02)
time.sleep(1)
print("----------------------------------------------------------------------------------\nADVENTURER REQUIRED!!!!!!\n\nTHE DUCK LORD HAS BECOME TO POWERFUL,\nSOMEBODY MUST DEFEAT HIM!!!")
time.sleep(0.75)
pressEnter()
pywriter.write("\n\nREWARD: Honor and Glory!", rate=0.05)
pywriter.write("\n...", rate=0.175)
pywriter.write("\n...", rate=0.175)
pywriter.write("\nand 9 trillion shmillion pigeon dollars", rate=0.03)
print("----------------------------------------------------------------------------------")

takeQuest = input("\nDo you accept this quest? ('yes' or 'no') ").lower()

if takeQuest != "yes":
    print("You change your mind and decide to take the quest anyway.")

pywriter.write("\n> Old Man Pigeon: I have managed to construct a portal to the Duck Lord's realm.", rate=0.1)
pywriter.write("> Old Man Pigeon: Enter the portal, defeat his bird henchmen, and kill the Duck Lord.", rate=0.1)
pressEnter()

pywriter.write("The old pigeon shows you a new sword technique to help you on your quest.", rate=0.05)
time.sleep(1.75)
pywriter.write("YOU LEARNED SLASH!", rate=0.05)
hasAtk2 = True

pressEnter()
pywriter.write("He leads you around to the backyard of his poorly constructed, wooden shack.", rate=0.02)
pywriter.write("A purple glowing portal with a rusted metal frame towers over you,", rate=0.02)
pywriter.write("it glows with such intensity that you have to shield your little pigeon eyes from it.", rate=0.02)

pressEnter()

pywriter.write("> Old Man Pigeon: Oh, and you'll want this.", rate=0.1)
pywriter.write("He hands you a bottle of a strange red liquid.", rate=0.02)
time.sleep(2)
pywriter.write("HEALTH POTION OBTAINED! Use for +50 HP", rate=0.02)

slot1 = "Health Potion"
hasHealthPot = True

pressEnter()

pywriter.write("You step into the portal.", rate=0.12)

# going into duck lord realm
print("\n*spooky music plays*\n")
time.sleep(1)
pywriter.write("The enormous tower looms over you, enveloping the burning red sun in its infinite shadow.", rate=0.065)
pywriter.write("You are standing on a floating island before the megastructure, one of many that make up the dimension.", rate=0.065)
pywriter.write("You look up and the eyes of the Duck Lord pierce your pigeon-y soul and strike fear into your little wings.", rate=0.065)

# Duck Realm Battle 1 Start
inBattle = True
dave = Dove()
Enemy = dave
Enemy.name = "Dave the Dove"
time.sleep(1)
# fight intro message
pywriter.write("\nThe Duck Lord throws down a dove from the top of the building and it crashes to the ground in front of you.", rate=0.01)
time.sleep(2)
pywriter.write("\n" + Enemy.name + " challenges you to a duel!", rate=0.01)
time.sleep(1)
pywriter.write("\n\nDOVE HP: " + str(Enemy.hp) + "\n\nYOUR HP: " + str(hp), rate=0.01)


time.sleep(2)
checkInputs()
# Duck Realm Battle 1 End

# Duck Realm Battle 2 Start
inBattle = True
carl = CanGoose()
Enemy = carl
Enemy.name = "Carl the Canadian Goose"
time.sleep(1)
# fight intro message
pywriter.write("\nThe Duck Lord chucks a canadian goose at you with such immense force your wing gets torn almost in half.", rate=0.01)
pywriter.write("\n(10 damage taken)", rate=0.01)
hp = hp - 10
time.sleep(2)
pywriter.write("\n" + Enemy.name + " challenges you to a duel!", rate=0.01)
time.sleep(1)
pywriter.write("\n\nGOOSE HP: " + str(Enemy.hp) + "\n\nYOUR HP: " + str(hp), rate=0.01)


time.sleep(2)
checkInputs()
# Duck Realm Battle 2 End

pywriter.write("The Duck Lord leaps from the tower and crashes down into the ground in front of you.", rate=0.053)
pywriter.write("You took 10 damage from the impact.", rate=0.01)
hp = hp - 10

# Duck Lord Battle Start
inBattle = True
ducklord = DuckLord()
Enemy = ducklord
Enemy.name = "The Duck Lord"
time.sleep(2)
pywriter.write("\n" + Enemy.name + " challenges you to a duel!", rate=0.01)
time.sleep(1)
pywriter.write("\n\nDUCK LORD HP: " + str(Enemy.hp) + "\n\nYOUR HP: " + str(hp), rate=0.01)


time.sleep(2)
checkInputs()
# Duck Lord Battle End

pywriter.write("YAHOO!!!! YOU DID IT!!!!", rate=0.035)
time.sleep(1)
pywriter.write("...", rate=0.15)
pywriter.write("ok go home now", rate=0.035)
exit()