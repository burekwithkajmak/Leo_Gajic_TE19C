onetime = 30
monthly = 900


def spårvagn(antal):
    price_onetime = antal * 30
    price_montly = 900
    if price_onetime > 900:
        print(f"Du åker spårvagn {antal} gånger och därför är det mer värt för dig att köpa ett månadskort")
    else:
        print(f"Du åker spårvagn {antal} gånger och därför är det mer värt för dig att köpa engångskort när du åker")

while True:
    try:
        åkturer = int(input("Hur många ånger åker du spårvagn?: "))
        assert åkturer > 0, "Du måste åka fler ånger än 0 gånger för att programmet ska kunna räkna ut"
        break
    except AssertionError as msg:
        print(msg)
    except:
        print("Du måste skriva tal och inte en string!")
        

spårvagn(åkturer)