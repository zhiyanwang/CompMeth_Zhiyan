import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(-x**2)

E_x = []
x = []

x_n = 0

for x_n in range(0,500):

    N = 30
    a = 0.0
    b = x_n/100
    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)

    for k in range(1,N):
        s += f(a+k*h)

    E_x.append(h*s)
    x.append(x_n/100)
    x_n += 1

print(len(x))
print(len(E_x))

plt.plot(x,E_x,"purple")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.title("E(x)")
plt.show()