import random
import os
import function
import time

Name = input("What is Your Hero's name? ")
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
Slot0 = {"0": 0, "Wood Helmet": 3}
b1 = 0
b2 = 0
b3 = 0
lvlp = 0

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
Slot = ["0", "Shirt", "Leggings", "Rookie's Sword", "0", "0", "0"]
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


def BuffName():
  global b1
  global b2
  global b3
  if b1 == 5:
    thing1 = "Armour Boost Lvl1"
  elif b1 == 10:
    thing1 = "Armour Boost Lvl2"
  else:
    thing1 = "None"

  if b2 == 5:
    thing2 = "Weapon Boost Lvl1"
  elif b2 == 10:
    thing2 = "Weapon Boost Lvl2"
  else:
    thing2 = "None"

  if b3 == 5:
    thing3 = "Crit Boost Lvl1"
  elif b3 == 15:
    thing3 = "Crit Boost Lvl2"
  else:
    thing3 = "None"
  return [thing1, thing2, thing3]

def fighttut1():
  global HP
  global MP
  global HPM
  global MPM
  EHP = 5
  EHPM = 5
  
  print("Enemy: Wolf")
  print("Wolf's HP: "  + str(EHP) + "/" + str(EHPM))
  print()
  print("Your HP: " + str(HP) + "/" + str(HPM))
  print("Your MP: " + str(MP) + "/" + str(MPM))
  print("press enter")
  input()
  os.system("clear")
  print("----INFORMATION----")
  print("Enemy: Wolf <--Name of enemy")
  print("Wolf's HP: "  + str(EHP) + "/" + str(EHPM)+" <-- enemy's health")
  print()
  print("Your HP: " + str(HP) + "/" + str(HPM)+" <-- Your health ")
  print("Your MP: " + str(MP) + "/" + str(MPM)+" <-- Your mana(this will be used later)")
  print("press enter")
  input()
  while EHP >= 1: 
    os.system("clear")
    print("Enemy: Wolf")
    print("Wolf's HP: "  + str(EHP) + "/" + str(EHPM))
    print()
    print("Your HP: " + str(HP) + "/" + str(HPM))
    print("Your MP: " + str(MP) + "/" + str(MPM))
    print("Attack or defend?")
    
    if input("1 = Attack, 2= defend") == 1:
      pass
      
      
  
  
buffs = BuffName()
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
print("Main weapon: " + str(Slot[3]))
print("Active buffs: " + buffs[0] + ", " + buffs[1] + ", " + buffs[2])

input("press enter to continue ")
os.system("clear")

print("You wander into the forrest...")
time.sleep(1)
os.system("clear")
print("As you stroll you hear a strange howl...")
time.sleep(1)
os.system("clear")
print("You see a Wolf!")
time.sleep(1)
os.system("clear")
fighttut1()


