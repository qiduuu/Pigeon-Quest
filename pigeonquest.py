import time

commands = "OPEN INVENTORY: inv, inventory\n VIEW STATS: stats\n"

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

def checkInputs():
    print("\n-------------------------------------\nCOMMAND LIST\n-------------------------------------\n" + commands + "-------------------------------------")
    if input("\n").lower() == "inv" or "inventory":
        print("\nInventory\n------------------------------------------\nSLOT 1: " + slot1 + "\nSLOT 2: " + slot2 + "\nSLOT 3: " + slot3 + "\n------------------------------------------")
    elif input('\n').lower() == "stats":
        print("HP: " + str(hp))
        print("LVL: " + str(level))
        print("XP: " + str(xp) + "/100")
    elif input('\n').lower() == ""


print("You are the last pigeon left.\nYour quest is to defeat the Duck Lord.\n\nYour journey begins now.")

time.sleep(2.5)
username = input("\nName your pigeon adventurer: ")

print("\n\n\nWelcome, " + username + ", to Pigeon Quest.")


