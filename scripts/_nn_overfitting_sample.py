#%matplotlib notebook
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import random
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def generate_set(size):
    return 6 * np.random.rand(size, 1) - 2

m = 50
x = generate_set(m)

noise =  np.random.randn(m, 1)

theta = [0.7, 2]

y = theta[0]*x**2 - theta[1]*x + 3 + noise 

def get_preds(x, y, degree):
    poly_feats = PolynomialFeatures(degree=degree, include_bias=False)
    x_poly = poly_feats.fit_transform(x)
    lr = LinearRegression()
    lr.fit(x_poly, y)
    return lr.predict(x_poly)

degrees = [2,   4,   8,   16,   32]
colors      = ['r', 'g', 'c', 'y', 'k']

plt.figure(figsize=(22, 6))
plt.scatter(x, y, marker='+', s=100, c='b' )

for degree, c in zip(degrees, colors):
    y_preds = get_preds(x, y, degree)
   
    plt.plot(
        sorted(x[:, 0]), 
        y_preds[np.argsort(x[:, 0])],
        c, 
        label= f'Model: {c}'
    )
    
#     print(
#     f'Degree: {degree}\n' 
#     f'RMSE:   {np.sqrt(mean_squared_error(y, y_preds)):.3f}\n' 
#     f'R2:     {r2_score(y, y_preds):.3f}'
#     '\n''-------------'
# )
    
plt.legend()
plt.grid(True)
plt.show()