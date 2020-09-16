#1
number = float(input("Ange ett tal för att se om de är positiv, negativt eller = noll: "))

if number > 0:
    print(f"Talet {number:.0f} är positivt")
elif number < 0:
    print(f"Talet {number:.0f} är negativt")
elif number == 0:
    print(f"Talet {number:.0f} är = 0")

#end

#2

number2 = float(input("Ange ett tal för att se om de är jämt, udda eller delbart med 5: "))

if number2%2 == 0:
    print(f"Talet {number2:.0f} är jämt")
elif number2%2 != 0:
    print(f"Talet {number2:.0f} är udda")
elif number2%5 ==0:
    print(f"Talet {number2:.0f} är delbart med 5")


#3

number1 = float(input("Ange ett tal kid"))
number2 = float(input("Ange ett tal kid"))
number3 = float(input("Ange ett tal kid"))
number4 = float(input("Ange ett tal kid"))

numbers = [number1, number2, number3, number4]

print("Största talet är", max(numbers))

#4

vinkel = float(input("Ange graderna på din vinkel för att se om den är trubbig, spetsig eller rät: "))

if vinkel == 90:
    print("Vinkeln är rät")
elif vinkel == 180:
    print("Vinkeln rak")
elif vinkel == 360:
    print("Vinkel är hel")
elif vinkel > 180:
    print("Vinkeln är konvex")
elif vinkel < 90:
    print("Vinkeln är spetsig")
elif vinkel > 90:
    print("Vinkeln är trubbig")