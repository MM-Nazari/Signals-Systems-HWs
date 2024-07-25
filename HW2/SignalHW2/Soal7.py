import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
t_start  = -5
t_finish = 5
t = np.arange(t_start, t_finish + 0.1, 0.1)
x = (3 * np.absolute(np.cos(7 * t))) + (3 * np.sin(pi * t))
plt.plot(t, x ,label="Signal")
plt.stem(t, x)
plt.legend()
plt.show()
# np.clip baraye mahdood kardane signal
t1 = np.ndarray.clip(t,0,5)
plt.plot(t1, x ,label="Limited")
plt.stem(t1, x)
plt.legend()
plt.show()
