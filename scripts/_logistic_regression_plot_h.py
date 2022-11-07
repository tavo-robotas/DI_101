import numpy as np
import matplotlib.pyplot as plt
A = 1
a = 3.5
x = np.linspace(0.01, 1, 100)
y = A * x**a

plt.figure(figsize=(20,10))
plt.plot(x, y, linewidth=2.5, color='navy', label='y=0')
plt.legend(loc='upper left')
plt.xlim(0, 1)
plt.xlabel(r'z')
plt.ylabel(r'cost')
ax.set_xticks([])
ax.set_yticks([])
plt.grid(True);
