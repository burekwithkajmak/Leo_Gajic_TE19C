import pandas as pd 

df = pd.read_csv("sysselsattning.csv")

df = df["2019"][0:12]

count = 0
summa = 0

for i in df:
    if count%2 != 0:
        summa = summa + i
    else:
        pass
    count = count + 1

print(f"Det är {summa} kvinnor som förvärvsarbetade i åldern 16-44 i Sverige år 2019")




