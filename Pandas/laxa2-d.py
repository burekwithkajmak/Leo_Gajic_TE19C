import pandas as pd 

df = pd.read_csv("sysselsattning.csv")

df = df["2019"][12:24]

count = 0
summa = 0

for i in df:
    if count%2 != 0:
        summa = summa + i
    else:
        pass
    count = count + 1

print(f"Det är {summa} kvinnor som inte förvärvsarbetade i åldern 16-44 i Sverige år 2019")




