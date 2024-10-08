
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

def checkUpgrades():
    if hasAtkUp1:
        dmg = 15
    if hasAtkUp2:
        dmg = 25
    if hasAtkUp3:
        dmg = 40

# Checks for user input on commands from the command variable above such as stats and inventory
def checkInputs():
    print("\n-------------------------------------\nCOMMAND LIST\n-------------------------------------\n" + commands + "-------------------------------------")
    userInput = input('\n').lower()
    if userInput == "inv" or userInput.lower() == "inventory":
        print("\nInventory\n------------------------------------------\nSLOT 1: " + slot1 + "\nSLOT 2: " + slot2 + "\nSLOT 3: " + slot3 + "\n------------------------------------------")
        time.sleep(1)
        checkInputs()
    elif userInput == "stats":
        print("HP: " + str(hp))
        print("LVL: " + str(level))
        print("XP: " + str(xp) + "/100")
        time.sleep(1)
        checkInputs()
    elif userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "stab" and inBattle == True:

        print("\nYou hit " + Enemy.name + " for " + str(dmg) + " damage!\n")
        Enemy.hp = Enemy.hp - dmg
        time.sleep(1)
        if Enemy.hp <= 0:
            print(Enemy.name + " has been vanquished! Congratulations!\n")
            print("You gained " + str(Enemy.xpGain) + " XP! :)")
            inBattle = False
        else:
            print(Enemy.name + " is now at " + str(Enemy.hp) + "hp")
            time.sleep(1)
            checkInputs()
    elif userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "stab" and inBattle == False:
        print("You are not in a battle right now. \n\n")
    else:
        print("Invalid command.\n\n")
        time.sleep(1)
        checkInputs()



print("You are the last pigeon left.\nYour quest is to defeat the Duck Lord.\n\nYour journey begins now.")

time.sleep(2.5)
username = input("\nName your pigeon adventurer: ")
print("\n\nWelcome, " + username + ", to Pigeon Quest.")

# Battle 1
inBattle = True
bob = Duckling()
Enemy = bob
Enemy.name = "Duckling Bob"
time.sleep(1)
# fight intro message
print("\nA little duck jumps out of a nearby bush holding a sword!")
time.sleep(2)
print("\n" + Enemy.name + " challenges you to a duel!\n\nDUCKLING HP: " + str(bob.hp) + "\n\nYOUR HP: " + str(hp))



time.sleep(3)
checkInputs()
