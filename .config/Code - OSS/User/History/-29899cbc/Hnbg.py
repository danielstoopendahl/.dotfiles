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

#plt.scatter(x, y, marker="+")


fittedpol = polynomial.polyfit(x, y, 5)
p2vals = polynomial.polyval(np.linspace(0,5,num=100), fittedpol)
print(fittedpol)
#plt.plot(np.linspace(0,5,num=100), p2vals)

xx = np.linspace(-10,10)
yy = polynomial.polyval(xx, fittedpol)
#plt.plot(xx, yy)
#plt.axis([0, 5, 3, 8])




# Uppgift 3
print("Uppgift 3")
x = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50])

y = np.array([1.31,1.66,1.72,1.91,1.96,2.00,2.32,2.51,2.50,2.34,2.38,2.35,2.50,2.94,2.71])

ny = np.exp(y)
#plt.scatter(x, y)

""" fittedpol = polynomial.polyfit(x, ny, 1)
xx = np.linspace(-1,2)
yy = polynomial.polyval(xx, fittedpol)
plt.plot(xx, np.log(yy))
print(fittedpol)
plt.show() """



# Uppgift 4
print("Uppgift 4")
v = np.loadtxt('race.txt')
print(v.size)
print(v[0])
print(v[450])

vprev = np.roll(v, -1)
v = np.where(v<80, v, vprev)

t = np.linspace(0,40, num=6000)

plt.plot(t, v)
plt.show()
print(max(v))

print(np.trapz(v,t))

data = requests.get('https://cs.lth.se/EDAA55/numpy/const_accel').text
with open('const_accel.txt', 'w') as f: f.write(data)