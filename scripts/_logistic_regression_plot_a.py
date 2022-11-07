import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("../data_samples/cells.csv")

plt.figure(figsize=(16,8))
plt.xlabel('lastelės dydis')
plt.ylabel('piktybinis navikas')
plt.scatter(data.cell_size, data.malignant, marker='o', s=50, color='red')
plt.grid(True);