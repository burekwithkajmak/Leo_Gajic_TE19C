numbers = []


while True:
    try:
        for i in range(1,6):
            tal = int(input(f"Ange ett tal {i}: "))
            numbers.append(tal)
    break
    except AssertionError as msg:
        print(msg)
    except:
        print("Du måste skriva ett tal och inte en string.")


