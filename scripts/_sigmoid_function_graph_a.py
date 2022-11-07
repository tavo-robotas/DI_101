import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

values = np.arange(-10, 10, 0.1)

plt.figure(figsize=(16,8))
plt.plot(values, sigmoid(values))
plt.axhline(y=1, color='blue', linestyle='dotted')
plt.axhline(y=0, color='blue', linestyle='dotted')
plt.axvline(x=0, color='red', linestyle='solid')
plt.text(0,0.5,'(0.5)', size=14)
plt.xlabel('z' , fontsize=14)
plt.ylabel('f(z)', fontsize=14)
plt.grid(True)