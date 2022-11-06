import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = [
    [x/12      + random.uniform(-1,1) for x in range(0,50)], 
    [2**(x/12) + random.uniform(-1,1) for x in range(0,50)]
]

theta = [0.2, 0.03, 0.7, 0.002, 0.04]
def var(i):
    return random.uniform(-(i[0]+i[1])/4,(i[0]+i[1])/4)

def y_of_x(xa):
    return theta[0]*xa[0]**2 + theta[1]*xa[0]*xa[1] + theta[2]*xa[0] + theta[3]*xa[1]**2 + theta[4]*xa[1] + 2.0 + var(xa)

Y = []
for xa in np.transpose(X):
    Y.append(y_of_x(xa))
    
fig = plt.figure(figsize=(12, 12))
ax = plt.axes(projection='3d')
ax.scatter3D(X[0], X[1], Y)
ax.set_xlabel('X0 Values')
ax.set_ylabel('X1 Values')
ax.set_zlabel('Y Values')
ax.grid(True)
