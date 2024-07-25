import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
pi = np.pi
# gereftan signal voroodi
N = int(input('enter N: '))
n = np.linspace(0, N - 1, N)
x = []
for i in n:
    e = float(input('enter x[' + str(int(i)) + ']: '))
    x.append(e)
x = np.array(x)
plt.stem(n, x, label="Signal Avalie")
plt.legend()
plt.show()


# mohasebe ak
def ak(k):
    w = (2 * pi) / N
    y = x * np.exp(k * -j * w * n)
    return (1 / N) * np.sum(y)

# M=1
M = 1
x1 = np.zeros((len(n),))
y1 = np.zeros((len(n),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * ((2 * pi) / N) * n)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.stem(n, np.real(x1), label="Fourier with M=1")
plt.legend()
plt.show()
# M=2
M = 2
x1 = np.zeros((len(n),))
y1 = np.zeros((len(n),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * ((2 * pi) / N) * n)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.stem(n, np.real(x1), label="Fourier with M=2")
plt.legend()
plt.show()
# M=5
M = 5
x1 = np.zeros((len(n),))
y1 = np.zeros((len(n),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * ((2 * pi) / N) * n)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.stem(n, np.real(x1), label="Fourier with M=5")
plt.legend()
plt.show()
# M=10
M = 10
x1 = np.zeros((len(n),))
y1 = np.zeros((len(n),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * ((2 * pi) / N) * n)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.stem(n, np.real(x1), label="Fourier with M=10")
plt.legend()
plt.show()
# M=50
M = 50
x1 = np.zeros((len(n),))
y1 = np.zeros((len(n),))
for k in range(-M, M + 1, 1):
    try:
        y1 = ak(k) * np.exp(k * j * ((2 * pi) / N) * n)
        np.add(x1, y1, out=x1, casting="unsafe")
    except ZeroDivisionError:
        continue
plt.stem(n, np.real(x1), label="Fourier with M=50")
plt.legend()
plt.show()
