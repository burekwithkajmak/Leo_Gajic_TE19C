#Tom dict
ListPokemon = {}

#filen
fil = open("pokemonlista.txt", "r")

def findPokemon():
    #Tom dict
    returnList = {}
    #loop som kör igenom varje element i txt dokumentet.
    for line in fil:
        LineSplit = line.split()
        #Här sätter jag upp dicten.
        returnList[LineSplit[1]] = 'Typ: '+LineSplit[2]+', Index:'+LineSplit[0]
    #return för att kunna använda senare.
    return returnList

#Ny variabel.
ListPokemon = findPokemon()

print(ListPokemon['Squirtle'])