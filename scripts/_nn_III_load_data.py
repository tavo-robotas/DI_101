import numpy as np
import matplotlib.pyplot as plt

points = np.array([[0,0],[0,1],[1,0],[1,1]])

plt.figure(figsize=(8,8))
for point in points:
    if point[0] == point[1]:
        marker = 'x'
        color  = 'red'
    else:
        marker = 'o'
        color  = 'blue'
    plt.scatter(point[0], point[1], marker=marker,c=color, s=300)
plt.xlabel('x1', fontsize=14)
plt.ylabel('x2', fontsize=14)
plt.grid(True)
plt.tight_layout()
