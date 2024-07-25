import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
t = np.arange(-5, 5 + 0.1, 0.1)
# cos(wt + theta)
w = (1/3) * pi
theta = (1/4) * pi
x1 = np.cos((w * t) + (theta))
plt.plot(t, x1 ,label="cos(wt + theta)")
plt.stem(t, x1)
plt.legend()
plt.show()
# |c|e**(rt)
c = 2
r = 1
x2 =  (np.absolute(c)) * (np.exp(r * t))
plt.plot(t, x2 ,label="|c|e**(rt)")
plt.stem(t, x2)
plt.legend()
plt.show()
# |c|e**(rt)cos(wt + theta)
x3 =  x2 * x1
plt.plot(t, x3 ,label="|c|e**(rt)cos(wt + theta)")
plt.stem(t, x3)
plt.legend()
plt.show()