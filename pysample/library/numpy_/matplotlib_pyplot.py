import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, math.pi * 2, 0.1)
siny = np.sin(x)
cosy = np.cos(x)

plt.plot(x, siny, label=" sin")
plt.plot(x, cosy, label=" cos")

plt.xlabel(" x")
plt.ylabel(" y")
plt.title(" sin, cos")
plt.legend()

plt.show()
