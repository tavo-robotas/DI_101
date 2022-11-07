import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 1, 100)
y = - np.log(x)

plt.figure(figsize=(20,10))
plt.plot(x, y, linewidth=2.5, color='navy', label='y=1')
plt.legend(loc='upper right')

plt.xlabel(r'z')
plt.ylabel(r'cost')
plt.grid(True);
