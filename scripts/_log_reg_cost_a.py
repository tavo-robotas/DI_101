import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 1, 100)
y = 1 - np.log(1 - x)

plt.figure(figsize=(20,10))
plt.plot(x, y, linewidth=2.5, color='navy', label='y=0')
plt.legend(loc='upper left')

plt.xlabel(r'z')
plt.ylabel(r'cost')
plt.grid(True);
