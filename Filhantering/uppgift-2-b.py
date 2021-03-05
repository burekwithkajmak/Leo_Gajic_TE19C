
fil = open("Provresultat.txt", "r")

lista = []

for line in fil:
    lista.append(line)

sorted_list = sorted(lista)
print(sorted_list)

with open('Provresultat.txt', 'w') as handlefile:
    handlefile.write("SORTERAT")
    for item in sorted_list:
        handlefile.write('%s\n' % item)









