import random as rnd

fil = open("simulering.txt","x")

exponent = int(input("Ange en exponent för 10^x: "))

antal_ettor = 0
antal_tvåor = 0
antal_treor = 0
antal_fyror = 0
antal_femmor = 0
antal_sexor = 0

simulator_start = 0

while simulator_start < exponent:
    simulator_start = simulator_start + 1
    for i in range(10**simulator_start):
        dice = rnd.randint(1,6)
        if dice == 6:
            antal_sexor = antal_sexor + 1
        elif dice == 5:
            antal_femmor = antal_femmor + 1
        elif dice == 4:
            antal_fyror = antal_fyror + 1
        elif dice == 3:
            antal_treor = antal_treor + 1
        elif dice == 2:
            antal_tvåor = antal_tvåor + 1
        else:
            antal_ettor = antal_ettor + 1

    sannolikhet_ettor = antal_ettor/(10**simulator_start)
    sannolikhet_tvåor = antal_tvåor/(10**simulator_start)
    sannolikhet_treor = antal_treor/(10**simulator_start)
    sannolikhet_fyror = antal_fyror/(10**simulator_start)
    sannolikhet_femmor = antal_femmor/(10**simulator_start)
    sannolikhet_sexor = antal_sexor/(10**simulator_start)

    fil.write(f"\nVid {10**simulator_start} kast ar : \nAntal ettor = {antal_ettor}, sannolikhet {sannolikhet_ettor} \nAntal tvaor = {antal_tvåor} , sannolikhet {sannolikhet_tvåor} \nAntal treor = {antal_treor}, sannolikhet {sannolikhet_treor} \nAntal fyror = {antal_fyror}, sannolikhet {sannolikhet_fyror} \nAntal femmor = {antal_femmor}, sannolikhet {sannolikhet_femmor} \nAntal Sexor = {antal_sexor}, sannolikhet {sannolikhet_sexor}")
    fil.write(f"\n")
    # print(f"Vid {10**simulator_start} kast är : Antal ettor = {antal_ettor}, sannolikhet {sannolikhet_ettor} Antal tvåor = {antal_tvåor} , sannolikhet {sannolikhet_tvåor} Antal treor = {antal_treor}, sannolikhet {sannolikhet_treor} Antal fyror = {antal_fyror}, sannolikhet {sannolikhet_fyror} Antal femmor = {antal_femmor}, sannolikhet {sannolikhet_femmor} Antal Sexor = {antal_sexor}, sannolikhet {sannolikhet_sexor}")
