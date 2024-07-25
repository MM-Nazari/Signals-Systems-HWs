import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
pi = np.pi
t = np.arange(-pi, pi + 0.1, 0.1)
# signal morede nazar ra dar zir vared mikonim be onvane mesal sin(2pit)
def x(t: np.ndarray):
  return np.sin(2 * pi * t)
# baraye chap az np.real estefade shode ke agar signal voroodi complex bood bakhash real an ra chap konad
# baraye signal haye haghighi ham farghi nemikonad
plt.stem(t, np.real(x(t)), label="Signal")
plt.legend()
plt.show()
odd = (x(t) - x(-t)) / 2
even = (x(t) + x(-t)) / 2
plt.stem(t, np.real(odd), label="odd")
plt.legend()
plt.show()
plt.stem(t, np.real(even), label="even")
plt.legend()
plt.show()