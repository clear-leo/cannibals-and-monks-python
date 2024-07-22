import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

island1 = {
    "cannibals":3,
    "monks":3
}
island2 = {
    "cannibals":0,
    "monks":0
}
boat = {
    "cannibals":0,
    "monks":0,
    "island":True
}
choice = None

print("There's two islands, if the amount of cannibals exceeds the amount of monks in an island (boat included) you lose.")
print("You can only move two people at a time")
print("Press enter to continue")
input()


while True:
    clear()
    print("Enter c if you want to move a cannibal to the boat, m if you want to move a monk to the boat, and b if you want to move the boat itself")
    if boat["island"] == True:
        print(f"The boat is on island 1")
    else:
        print(f"The boat is on island 2")
    print(f"island 1: {island1["cannibals"]} cannibals, {island1["monks"]} monks")
    print(f"island 2: {island2["cannibals"]} cannibals, {island2["monks"]} monks")
    print(f"boat: {boat["cannibals"]} cannibals, {boat["monks"]} monks")
    
    choice = input().lower()
    match choice:
        case "c":
            print("What do you choose to do with the cannibals? (load / ground)")
            choice = input().lower()
            if choice == "load":
                if boat["island"] == True and island1["cannibals"] != 0 and boat["cannibals"] + boat["monks"] < 2:
                    island1["cannibals"] -= 1
                    boat["cannibals"] += 1
                elif boat["island"] == False and island2["cannibals"] != 0 and boat["cannibals"] + boat["monks"] < 2:
                    island2["cannibals"] -= 1
                    boat["cannibals"] += 1
            elif choice == "ground":
                if boat["island"] == True and boat["cannibals"] + boat["monks"] > 0:
                    island1["cannibals"] += 1
                    boat["cannibals"] -= 1
                elif boat["island"] == False and boat["cannibals"] + boat["monks"] > 0:
                    island2["cannibals"] += 1
                    boat["cannibals"] -= 1

        case "m":
            print("What do you choose to do with the monks? (load / ground)")
            choice = input().lower()
            if choice == "load":
                if boat["island"] == True and island1["monks"] != 0 and boat["cannibals"] + boat["monks"] < 2:
                    island1["monks"] -= 1
                    boat["monks"] += 1
                elif boat["island"] == False and island2["monks"] != 0 and boat["cannibals"] + boat["monks"] < 2:
                    island2["monks"] -= 1
                    boat["monks"] += 1
            elif choice == "ground":
                if boat["island"] == True and boat["cannibals"] + boat["monks"] > 0:
                    island1["monks"] += 1
                    boat["monks"] -= 1
                elif boat["island"] == False and boat["cannibals"] + boat["monks"] > 0:
                    island2["monks"] += 1
                    boat["monks"] -= 1

        case "b":
            boat["island"] = not boat["island"]

        case _:
            pass
    
    #Island logic!
    if island1["monks"] != 0 and island1["cannibals"] > island1["monks"] and boat["island"] == False:
        print("The cannibals ate the monks in island 1")
        break
    if island2["monks"] != 0 and island2["cannibals"] > island2["monks"] and boat["island"] == True:
        print("The cannibals ate the monks in island 2")
        break

    if boat["monks"] != 0 and island1["cannibals"] > boat["monks"] + island1["monks"] and boat["island"] == True:
        print("The cannibals ate the monks in island 1")
        break
    if boat["monks"] != 0 and island2["cannibals"] > boat["monks"] + island2["monks"] and boat["island"] == False:
        print("The cannibals ate the monks in island 2")
        break