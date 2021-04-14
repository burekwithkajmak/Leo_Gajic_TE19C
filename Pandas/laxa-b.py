import pandas as pd 

df = pd.read_csv("sysselsattning.csv")

df = df["2019"][12:24]

summa = 0

for i in df:
    summa = summa + i

print(f"Det är {summa} i åldern 16-44 som inte förvärvsarbetade i Sverige år 2019")


