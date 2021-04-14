import matplotlib.pyplot as plt
import pandas as pd 

headers = ["förvärvsarbetande", "ej förvärvsarbetande"]

df = pd.read_csv("sysselsattning.csv")


df1 = df["2019"][0:12]
df2 = df["2019"][12:24]

summa1 = 0
summa2 = 0

for a,b in zip(df1,df2):
    summa1 = summa1 + a 
    summa2 = summa2 + b


print(summa1)
print(summa2)


labels = 'Förvärvsarbetade', 'Icke förvärvsarbetade'
storlek = [summa1,summa2]
explode = (0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(storlek, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()



