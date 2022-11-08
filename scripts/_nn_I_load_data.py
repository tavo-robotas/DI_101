import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data_samples/data_blobs_nonlin_b.csv')

plt.figure(figsize=(16,8))
plt.scatter(data.x1, data.x2, c=data.y);
plt.xlabel('X1')
plt.ylabel('X2')
plt.tight_layout()
