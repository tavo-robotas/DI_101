import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(12,12))
x3, y3 = np.random.multivariate_normal([0,0], [[.5,0],[0,.5]] , 20).T
t = np.linspace(0,2*np.pi,20)

ax.plot((3+x3)*np.sin(t), (3+y3)*np.cos(t), "o")
ax.plot(x3, y3, "P")

xb1 = np.linspace(-5.0, 5.0, 100)
xb2 = np.linspace(-5.0, 5.0, 100)
Xb1, Xb2 = np.meshgrid(xb1,xb2)
b = -1 + Xb1**2 + Xb2**2
ax.set_xlabel('x1', fontsize=14)
ax.set_ylabel('x2', fontsize=14)
ax.axhline(y=0, color='black', linestyle='solid')
ax.axvline(x=0, color='black', linestyle='solid')

ax.axis('equal')