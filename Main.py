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
Crit = 4
Coins = 10
Slot0 = {"0": 0, "WoodHelmet": 3}
b1 = 0
b2 = 0
b3 = 0
#Slots are numbered in the id of the list
Slot1 = {"Shirt": 2}
Slot2 = {"Leggings": 1, "Plated Leggings": 3}
Slot3 = {"Rookie's Sword": 5, "Sword": 8}
SlotBuff = {
  "0": 0,
  "Crit1": 5,
  "Crit2": 10,
  "Def1": 5,
  "Def2": 15,
  "Dam1": 10,
  "Dam2": 20
}
#SlotBuff is slot 4,5 and 6
Slot = ["0", "Shirt", "Leggings", "Wood Sword", "0", "0", "0"]
DAM = Slot3.get(Slot[3]) + BDAM
DEF = Slot0.get(Slot[0]) + Slot1.get(Slot[1]) + Slot2.get(Slot[2])
BUFF = [
  SlotBuff.get(Slot[4]),
  SlotBuff.get(Slot[5]),
  SlotBuff.get(Slot[6]),
]


def Modbuff():
  global b1
  global b2
  global b3
  global BUFF
  if BUFF[0] == 0 and BUFF[1] == 0 and BUFF[2] == 0:
    b1 = 0
    b2 = 0
    b3 = 0
  else:
    if BUFF[0] == 5:
      b1 = 5
    else:
      if BUFF[0] == 10:
        b1 = 10

    if BUFF[1] == 5:
      b2 = 5
    else:
      if BUFF[1] == 15:
        b2 = 15
    if BUFF[2] == 10:
      b3 = 10
    else:
      if BUFF[2] == 15:
        b3 = 15


os.system("clear")
print("Hero Stats")
print("Name: " + Name)
print("HP: " + str(HP) + "/" + str(HPM))
print("MP: " + str(MP) + "/" + str(MPM))
print("Lvl: " + str(Lvl))
print("XP: " + str(XP) + "/" + str(XPlvl))
print("Defense: " + str(DEF))
print("Crit chance: " + str(Crit) + "%")
print("Damage: " + str(DAM), "\033[33m")
print("Coins:" + str(Coins), "\033[0m")
print("Main weapon: "+ Slot[3])

input("press enter to continue")
os.system("clear")
