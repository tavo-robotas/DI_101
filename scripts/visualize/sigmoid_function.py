import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

x  = np.linspace(-10, 10)
y  = sigmoid(x)

plt.figure(figsize=(12,6))
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.plot(x, y, label='sigmoid');
plt.axvline(x=0 , c='r', ls='--' )
#plt.axhline(y=0.5 , c='b', ls='-.')

plt.grid(True)
