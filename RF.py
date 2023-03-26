import math
import matplotlib.pyplot as plt
import numpy as np
import timeit

x = np.array(range(-6,6))
y = x**3 + 3*x - 5
plt.plot(x,y)
plt.grid()
plt.show()

def f(x):
    return x**3+3*x-5


def regula(a,b):
    x = 0
    i=1
    condition = True
    while condition:
        n = str(x)
        x = a - ((b-a)/(f(b)-f(a)))*f(a)
        if f(x)<0:
            a=x
        else:
            b=x
        print("Iteration number: ", i, "     x = ",x, "     f(x) = ",f(x))

        m = str(x)
        if m[0:t+3]==n[0:t+3]:
            condition = False
        else:
            condition = True
            i = i+1
    
    print("Root found at x = ", x)
    print("Time taken: ",timeit.timeit())


a = input("First approximation root: ")
b = input("Second approximation root: ")
t = input("Enter precision of decimal places: ")
a = float(a)
b = float(b)
t = int(t)

if f(a)*f(b)>0:
    print("Given appproximation roots do not give a solution")
    print("Try again with different values")
else:
    regula(a,b)