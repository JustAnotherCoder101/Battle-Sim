import random
import os
import function

Name = input("What is Your Hero's name?")
HP = 20
MP = 20
HPM = 20
MPM = 20
XP = 0
XPlvl = 10
Lvl = 1
BDAM = 3
Coins = 10
Slot0 = {"0": 0}
Slot1 = {"Shirt": 2}
Slot2= {"Leggings": 1}
Slot3 = {"Twig": 5}
Slot4 = {"0": 0}
Slot = ["0", "Shirt", "Leggings", "Twig", "0"]
DAM = Slot3.get(Slot[3]) + BDAM
DEF = Slot0.get(Slot[0]) + Slot1.get(Slot[1]) + Slot2.get(Slot[2]) + Slot4.get(Slot[4])
os.system("clear")
print("Hero Stats")
print("Name: " + Name)
print("HP: " + str(HP) + "/" + str(HPM))
print("MP: " + str(MP) + "/" + str(MPM))
print("Lvl: " + str(Lvl))
print("XP: " + str(XP) + "/" + str(XPlvl))
print("Defense: " + str(DEF))
print("Damage: " + str(DAM))
print("Coins:" + str(Coins))
input("press enter to continue")
os.system("clear")
function.load(5)
