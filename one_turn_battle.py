#simulates a one turn battle between an attacker and defender

import random
import math

#get seed
user_seed = int(input("Enter the seed to run the fight with: "))
random.seed(user_seed)

#get attacker inputs
hp_a = int(input("Enter the attacker's hp: "))
strength_a = int(input("Enter the attacker's strength: "))
accuracy_a = int(input("Enter the attacker's accuracy: "))
crit_a = int(input("Enter the attacker's crit chance: "))
dodge_a = int(input("Enter the attacker's dodge rate: "))

#get defender inputs
hp_d = int(input("Enter the defender's hp: "))
strength_d = int(input("Enter the defender's strength: "))
accuracy_d = int(input("Enter the defender's accuracy: "))
crit_d = int(input("Enter the defender's crit chance: "))
dodge_d = int(input("Enter the defender's dodge rate: "))

#ask if defender is guarding
guard = input("Is the defender guarding? Y for yes, n for no: ").lower()

#generate random number 0-100
def roll():
    roll_number = round(random.random() * 100)
#   print(roll_number)
    return roll_number

#run attacker critical attack
def roll_critical_a():
    global hp_d
    if roll() <= crit_a:
        hp_d -= strength_a + 1
        print(f"attacker crit defender for {strength_a + 1} points of damage")
        check_hp_d()
    else:
        roll_attack_a()

#run defender critical attack
def roll_critical_d():
    global hp_a
    if roll() <= crit_d:
        hp_a -= strength_d + 1
        print(f"defender crit attacker for {strength_d + 1} points of damage")
        finish()
    else:
        roll_attack_d()

#run attacker attack
def roll_attack_a():
    if roll() <= accuracy_a:
        roll_dodge_d()
    else:
        print("attacker missed defender")
        roll_critical_d()

#run defender attack
def roll_attack_d():
    if roll() <= accuracy_d:
        roll_dodge_a()
    else:
        print("defender missed attacker")
        finish()

#run attacker dodge
def roll_dodge_a():
    global hp_a
    if roll() <= dodge_a:
        print("attacker dodged defender's attack")
        finish()
    else:
        dmg_d = random.randint(math.floor(strength_d / 2), strength_d)
        hp_a -= dmg_d
        print(f"defender hit attacker for {dmg_d} points of damage")
        finish()

#run defender dodge
def roll_dodge_d():
    global hp_d
    if roll() <= dodge_d:
        print("defender dodged attacker's attack")
        roll_critical_d()
    else:
        dmg_a = random.randint(math.floor(strength_a / 2), strength_a)
        hp_d -= dmg_a
        print(f"attacker hit defender for {dmg_a} points of damage")
        check_hp_d()

#check defender hp
def check_hp_d():
    if hp_d > 0 and guard == "y":
        roll_critical_d()
    else:
        finish()

#round negative hp to 0 and print results
def finish():
    global hp_a
    global hp_d
    if hp_a < 0:
        hp_a = 0
    if hp_d < 0:
        hp_d = 0
    print(f"After fighting the attacker has {hp_a} hp left and the defender has {hp_d} hp left")

roll_critical_a()
