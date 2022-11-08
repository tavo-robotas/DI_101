import numpy as np
import matplotlib.pyplot as plt

m = 50
X = np.asarray(m * [[1.5, 0. ]] +
               m * [[-1.5, 0.]] +
               m * [[0., -1.5]] +
               m * [[0., 1.5 ]]
)
X += .5 * np.random.randn(*X.shape)
y = np.concatenate((np.zeros(2*m), np.ones(2*m)))
plt.figure(figsize=(18,18))
plt.scatter(x=X[:,0], y=X[:,1], s=50, c=y);
plt.grid(True)
plt.tight_layout()