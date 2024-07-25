import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
pi = np.pi
# main Signal
t = np.arange(-1, 5 + 0.01, 0.01)
f1 = lambda t: 0
f2 = lambda t: -1
f3 = lambda t: 0
f4 = lambda t: 1
fx = np.piecewise(t, [(t > -1) * (t <= +1), (t > 1) * (t < 2), (t >= 2) * (t <= 4), (t > 4) * (t < 5)],
                  [f1, f2, f3, f4])
plt.plot(t, fx, label="Signal Avalie")
plt.legend()
plt.show()


# fourier
def ak(k):
    w = 2 * np.pi / 6
    x = fx * np.exp(-k * j * w * t)
    return (1 / 6) * np.sum(x) * 0.01


# M=1
M = 1
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=1")
plt.legend()
plt.show()
# M=2
M = 2
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=2")
plt.legend()
plt.show()
# M=5
M = 5
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=5")
plt.legend()
plt.show()
# M=10
M = 10
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=10")
plt.legend()
plt.show()
# M=50
M = 50
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=50")
plt.legend()
plt.show()
# M=100
M = 100
x1 = np.zeros((len(t),))
y1 = np.zeros((len(t),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * (2 * np.pi / 6) * t)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.plot(t, np.real(x1), label="Fourier with M=100")
plt.legend()
plt.show()
