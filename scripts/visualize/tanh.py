import numpy as np
import matplotlib.pyplot as plt


def tanh(x):
  return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

def _tanh(x):
  return 1 - htan(x) * htan(x)

x = np.linspace(-10,10,100)
y = tanh(x)

plt.figure(figsize=(12,6))
plt.plot(x, y)
plt.axvline(x=0 , c='r', ls='--' )
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.grid(True)
