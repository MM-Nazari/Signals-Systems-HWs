import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
pi = np.pi
# a
t1 = np.arange(-(2/3) * pi, (2/3) * pi + 0.1, 0.1)
x1 = np.exp(1.5 * j * t1)
plt.plot(t1, np.real(x1) ,label="e**(j(3/7)n)")
plt.stem(t1, np.real(x1))
plt.legend()
plt.show()
#b
t2 = np.arange(-1.5, 1.5 + 0.05, 0.05)
x2 = np.absolute(np.sin((2/3) * pi * t2)) + np.cos((4/3) * pi * t2)
plt.plot(t2, x2 ,label="|sin((2/3)pit)| + cos((4/3)pit)")
plt.stem(t2, x2)
plt.legend()
plt.show()
#c
t3 = np.arange(-3, 3 + 0.1, 0.1)
x3 = np.exp((1/3) * pi * j * t3) + np.exp((4/3) * pi * j * t3)
plt.plot(t3, np.real(x3) ,label="e**(j(1/3)pin) + e**(j(4/3)pin)")
plt.stem(t3, np.real(x3))
plt.legend()
plt.show()
#d
# cos(9t)
t4 = np.arange(-(1/9) * pi, (1/9) * pi + 0.02, 0.02)
x4 = np.cos((9) * t4)
plt.plot(t4, x4 ,label="cos(9t)")
plt.stem(t4, x4)
plt.legend()
plt.show()
# sin(2pit)
t5 = np.arange(-(1/2), (1/2) + 0.02, 0.02)
x5 = np.sin((2) * pi * t5)
plt.plot(t5, x5 ,label="sin(2pit)")
plt.stem(t5, x5)
plt.legend()
plt.show()
# cos(9t) + sin(2pit)
t6 = np.arange(-(4), (4) + 0.07, 0.07)
x6 = np.cos(9 * t6) + np.sin((2) * pi * t6)
plt.plot(t6, x6 ,label="cos(9t) + sin(2pit)")
plt.stem(t6, x6)
plt.legend()
plt.show()

