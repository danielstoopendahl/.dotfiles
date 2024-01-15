import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynomial
from scipy.integrate import solve_ivp #ivp = initial value problem
import requests

# Uppgift 1
print("Uppgift 1")
def yprime(t, y):
    return 9*t + 4*np.sin(3*t) - 5*y**2

solution = solve_ivp(yprime, [1,10], [7.])


print(solution)
""" 
plt.plot(solution.t, solution.y[0])
plt.show()
 """
# Uppgift 2
print("Uppgift 2")
x = np.array([ 0.000, 1.000, 2.000, 3.000, 4.000, 5.000 ])
y = np.array([ 3.749, 4.689, 6.273, 5.897, 6.381, 7.003 ])

plt.scatter(x, y, marker="+")


fittedpol = polynomial.polyfit(x, y, 5)
p2vals = polynomial.polyval(np.linspace(0,5,num=100), fittedpol)
print(fittedpol)
#plt.plot(np.linspace(0,5,num=100), p2vals)

xx = np.linspace(-10,10)
yy = polynomial.polyval(xx, fittedpol)
plt.plot(xx, yy)
plt.axis([0, 5, 3, 8])

plt.show()
