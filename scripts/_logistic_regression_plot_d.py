
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("../data_samples/cells.csv")
x  = data.drop('malignant',1)
y  = data.malignant

lr = LogisticRegression()
lr.fit(x,y)
y_p = lr.predict(x)

m = lr.coef_[0,0]
b = lr.intercept_[0]
lgs_curve = lambda x: 1/(1 + np.e**(-(m*x+b)))  
x_values = np.linspace(x.min(), x.max(), 1000)
y_values = lgs_curve(x_values)

plt.figure(figsize=(16,8))
plt.plot(x_values, y_values)
plt.scatter(data.cell_size, data.malignant, marker='o', s=50, color='red', label='duomenys')
plt.axhline(y=0.5, color='red', linestyle='dashed')
plt.grid(True)


print(f'coefficients: {lr.coef_}')
print(f'probabilties: {y_p}')