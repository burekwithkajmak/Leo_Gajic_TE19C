
print("Uppgift 1a")
for i in range(1,11):
    print(i)

print("Uppgift 1b")
for i in range(-10,11):
    print(i)
print("Uppgift 1c")

for i in range(10,-1,-1):
    print(i)
print("Uppgift 2")

for x in range(1,101):
    total = 0
    for g in range(2,(x//3)):
        if x%g==0:
            total = total +1
            break
    if total== 0 and x !=1:
        print(x)

print("Uppgift 3")
s = 0
for i in range(101):
    s += i
print(f"1+2+3.....+99+100 = {s}")
