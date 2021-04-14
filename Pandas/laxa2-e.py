import matplotlib.pyplot as plt
import pandas as pd 

headers = ["förvärvsarbetande", "ej förvärvsarbetande"]

df = pd.read_csv("sysselsattning.csv")

df1 = df["2019"][0:12]
df2 = df["2019"][12:24]

count = 0
sum_men_work = 0
sum_men = 0
sum_women_work = 0
sum_women = 0

#Antalet män som jobbar
for a in df1:
    if count%2 == 0:
        sum_men_work = sum_men_work + a
    else:
        pass
    count = count + 1
print(sum_men_work)

#Antalet kvinnor som jobbar
for b in df1:
    if count%2 != 0:
        sum_women_work = sum_women_work + b
    else:
        pass
    count = count + 1
print(sum_women_work)

#Antalet män som inte jobbar
for c in df2:
    if count%2 == 0:
        sum_men = sum_men + c
    else:
        pass
    count = count + 1
print(sum_men)

#Antalet kvinnor som inte jobbar
for d in df2:
    if count%2 != 0:
        sum_women = sum_women + d
    else:
        pass
    count = count + 1
print(sum_women)


titles = ["Män förvärvsarbetande", "Kvinnor förvärvsarbetande", "Män icke förvärvsarbetande", "Kvinnor icke förvärvsarbetande"]
resultat = [sum_men_work,sum_women_work,sum_men,sum_women]
plt.bar(titles, resultat, width=0.3)
plt.title("Förvärvsarbetande")
plt.xlabel("Sysselsättning")
plt.ylabel("Antal / (10^6)")
plt.show()





