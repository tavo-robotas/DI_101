import numpy as np
import matplotlib.pyplot as plt

def elu(z,alpha):
	return np.where(z < 0, alpha * (np.exp(z) - 1), z)

x = np.linspace(-10, 10, 1000)
y = elu(x, 1)

plt.figure(figsize=(12,6))
plt.xlabel('z', fontsize=14)
plt.ylabel('g(z)', fontsize=14)
plt.plot(x, y)
plt.grid(True)