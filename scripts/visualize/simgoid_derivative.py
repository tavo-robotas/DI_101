import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def _sigmoid(x):
    return sigmoid(x)*(1 - sigmoid(x))

x  = np.linspace(-10, 10)
y  = sigmoid(x)
_y = _sigmoid(x)

plt.figure(figsize=(12,6))
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.plot(x, y, label='sigmoid');
plt.plot(x, _y, label='derivative');
plt.axvline(x=0 , c='r', ls='--' )
#plt.axhline(y=0.5 , c='b', ls='-.')
plt.legend()
plt.grid(True)
