import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt 


X, y = make_blobs(
    n_samples=100,
    n_features=2,
    centers=2,
    center_box=(100, 150), 
    cluster_std=20
)
    
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=y)

plt.figure(figsize=(12,8))
plt.scatter(X[:,0], X[:,1], c=y)
plt.grid(True)