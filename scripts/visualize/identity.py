import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = x

plt.figure(figsize=(12,6))
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.plot(x, y)
plt.grid(True)