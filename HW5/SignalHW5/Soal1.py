import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
pi = np.pi
# gereftan signal voroodi
N = int(input('enter N: '))
n = np.linspace(0, N-1 , N)
x = []
for i in n:
    e = float(input('enter x[' + str(int(i)) + ']: '))
    x.append(e)
x = np.array(x)

# mohasebe ak
def ak(x, k):
    w = (2 * pi) / N
    sum = 0
    for n0 in range (0, N, 1) :
        try:
            y = x[n0] * np.exp(k * -j * w * n0)
            sum += y
        except ZeroDivisionError:
            continue
    return (1/N) * sum

# chape ak dar signal
for i in range (0, N, 1) :
    print("ak[{}] :".format(i), ak(x, i))

