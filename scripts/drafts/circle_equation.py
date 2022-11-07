import numpy as np
import matplotlib.pyplot as plt

def generate_set(size):
    return 6 * np.random.rand(size, 1) - 2
m  = 40
noise =  np.random.randn(m, 1)
x1 = generate_set(m)
x2 = generate_set(m)

xx = np.linspace(int(x1.min()), int(x1.max()), 20)
yy = np.linspace(int(x2.min()), int(x2.max()), 20)
xx, yy = np.meshgrid(xx,yy)
c = -1 + xx**2 + yy**2 
plt.figure(figsize=(16,16))
plt.scatter(x1, x2)
plt.contour(xx,yy,c,[0])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()