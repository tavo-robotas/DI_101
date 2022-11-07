import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("../data_samples/perceptron_data_reduced.csv")
x1  = data.X1
x2  = data.X2
y   = data.y

X   = data.drop('y', axis=1).values
X   = np.insert(X, 0, 1, axis=1)

lr = LogisticRegression()
lr.fit(X,y)
y_p = lr.predict(X)

theta = np.array([-5, 1, 1]).reshape(-1,1)

def hypothesis(X, theta):
    return X@theta

def predict(X, theta, p_thr = 0.5):
    y_pred = hypothesis(X, theta)
    return [1 if i > p_thr else 0 for i in y_pred]


def decision_boundary():
    for i in data.index:
       if data.X1[i] + data.X2[i] >= 5:
        
        print(f'point:{data.X1[i], data.X2[i]}')

decision_boundary()
        
y_pred = predict(X, theta)

plt.figure(figsize=(16,8))
plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.scatter(x1, x2, marker='o', s=50, c=y, label='duomenys')
plt.grid(True);



print(f'predictions: {y_pred}')
print(f'coefficients: {lr.coef_}')
print(f'probabilties: {y_p}')