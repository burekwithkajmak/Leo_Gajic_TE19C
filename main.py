#K-C

k = float(input("Ange temperatur i Kelvin: "))

c = k-273.15

print(f"{k} Kelvin är {c:.0f} Celsius

#C-K

c = float(input("Ange temperatur i Celsius: "))

k = c+273.15

print(f"{c} Celsius är {k:.0f} Kelvin")

#Västrafik

amount = float(input("Hur många gånger åker du med västtrafik: "))

enbiljet = 30

total = amount*enbiljet

print(f"Du betalar {total}kr om du åker med västraffik {amount:.0f}ggr")

if amount < 25:
    print(f"köp engånsbiljett")
else:
    print(f"Köp månadskort")


prin



