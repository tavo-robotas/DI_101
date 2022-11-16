import numpy as np
import matplotlib.pyplot as plt


def htanh(x):
  return np.maximum(-1, np.minimum(1, x))

x = np.linspace(-10,10,10)
y = htanh(x)

plt.figure(figsize=(12,6))
plt.plot(x, y)
plt.axvline(x=0 , c='r', ls='--' )
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.grid(True)
