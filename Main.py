import random
import os
import function

Name = input("What is Your Hero's name?")
HP = 100
MP = 50
HPM = 100
MPM = 50
XP = 0
XPlvl = 10
Lvl = 1
os.system("clear")
print("Hero Stats")
print("Name: " + Name)
print("HP: " + str(HP) + "/" + str(HPM))
print("MP: " + str(MP) + "/" + str(MPM))
print("Lvl: " + str(Lvl))
print("XP: " + str(XP) + "/" + str(XPlvl))
input("press enter to continue")
os.system("clear")
function.load(5)