import random as rnd 

frekvensTabell = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

for i in range(10**6):
    dice = rnd.randint(1,6)
    if dice in frekvensTabell:
        frekvensTabell[dice] = frekvensTabell[dice] + 1

print("Frekvestabell")
for key in frekvensTabell:
    print(str(key) +": " + str(frekvensTabell[key]))
