#Uppgift 3
import numpy as np 
import matplotlib.pyplot as plt


def f(x):
  return 3*x+1

x = np.arange(0,11,1)
y = []


for i in x:
  y.append(f(i))

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# print(x)
# print(y)
