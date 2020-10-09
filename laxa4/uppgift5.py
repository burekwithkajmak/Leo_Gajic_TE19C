#Uppgift 5

import random as rnd 

randomizer = rnd.randint(1,100)
print(randomizer)

guess = float(input("Gissa på ett heltal mellan 1-100: "))

while not guess == randomizer:
    if guess != randomizer:
        if guess > randomizer:
            print('Ledtråd : Du gissade för högt och det var fel!')
            guess = float(input("Gissa på ett heltal mellan 1-100: "))
        elif guess < randomizer:
            print('Ledtråd : Du gissade för lågt och det var fel')
            guess = float(input("Gissa på ett heltal mellan 1-100: "))
print('Du gissade rätt')
    