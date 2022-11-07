import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("../data_samples/cells_c.csv")
x  = data.drop('malignant',1)
y  = data.malignant

re = LinearRegression()
re.fit(x,y)
y_p = re.predict(x)

plt.figure(figsize=(16,8))
plt.scatter(data.cell_size, data.malignant, marker='o', s=30, color='red', label='duomenys')
plt.axhline(y=0.5, color='red', linestyle='dashed', label='slenkstis')
plt.axvline(x=40, color='blue', linestyle='dashed', label='x')
plt.plot(x, y_p, label='hipotezė');
plt.legend()
plt.grid(True);
print(f'coefficients: {re.coef_}, intercept: {re.intercept_}')