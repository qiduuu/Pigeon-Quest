import time

commands = "OPEN INVENTORY: inv, inventory\nVIEW STATS: stats\nATTACK: attack, atk, hit, stab\n"

hp = 100
xp = 0
level = 0

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

class Duckling:
    hp = 10
    dmg = 5
    name = "Duckling"
    xpGain = 10
class Swan:
    hp = 15
    dmg = 10
    name = "Swan"
    xpGain = 15
class CanGoose:
    hp = 25
    dmg = 15
    name = "Canadian Goose"
    xpGain = 25
class Dove:
    hp = 20
    dmg = 10
    name = "Dove"
    xpGain = 20
class Puffin:
    hp = 50
    dmg = 20
    name = "Puffin"
    xpGain = 50

# Checks for user input on commands from the command variable above such as stats and inventory
def checkInputs():
    print("\n-------------------------------------\nCOMMAND LIST\n-------------------------------------\n" + commands + "-------------------------------------")
    userInput = input('\n').lower()
    if userInput == "inv" or userInput.lower() == "inventory":
        print("\nInventory\n------------------------------------------\nSLOT 1: " + slot1 + "\nSLOT 2: " + slot2 + "\nSLOT 3: " + slot3 + "\n------------------------------------------")
    elif userInput == "stats":
        print("HP: " + str(hp))
        print("LVL: " + str(level))
        print("XP: " + str(xp) + "/100")
    elif userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "slash" and inBattle == True:
        print("You hit " + Enemy.name + " for 10 damage! \n" + Enemy.name + " is now at " + str(Enemy.hp - 10) + "hp")
        if Enemy.hp <= 0:
            print(Enemy.name + " has been vanquished! Congratulations!\n")
            print("You gained " + str(Enemy.xpGain) + " XP! :)")
    elif userInput == "attack" or userInput == "atk" or userInput == "hit" or userInput == "slash" and inBattle == False:
        print("You are not in a battle right now. \n\n")
    else:
        print("Invalid command.\n\n")
        checkInputs() 



print("You are the last pigeon left.\nYour quest is to defeat the Duck Lord.\n\nYour journey begins now.")

time.sleep(2.5)
username = input("\nName your pigeon adventurer: ")
bob = Duckling()
print("\n\n\nWelcome, " + username + ", to Pigeon Quest.")
time.sleep(1)
print("A little duck jumps out of a nearby bush holding a sword!")
time.sleep(2)
print("Duckling Bob challenges you to a duel!\n\nDUCKLING HP: " + str(bob.hp) + "\n\nYOUR HP: " + str(hp))
inBattle = True
Enemy = bob
Enemy.name = "Duckling Bob"

time.sleep(3)
checkInputs()
