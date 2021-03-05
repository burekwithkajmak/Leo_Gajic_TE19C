fil = open("diceRoll.txt","x")

import random as rnd

dices = []
dices_sorted = []
antalfemmor = 0

for i in range(1,11):
    dice = rnd.randint(1,6)
    dices.append(dice)
    dices_sorted.append(dice)
    dices_sorted.sort()
    if dice == 5:
        antalfemmor = antalfemmor + 1

fil.write(f"Simulera 10 tarningskast: {dices} ")
fil.write(f"\nKasten sorterade: {dices_sorted} ")
fil.write(f"\nAntalet femmor: {antalfemmor}")
