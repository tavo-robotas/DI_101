from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(
        n_samples=100, 
        n_classes=2,
        n_features=2, 
        n_informative=2, 
        n_redundant=0,
        random_state=0,
        n_clusters_per_class=2,
        flip_y=0.25
)
plt.figure(figsize=(16,8))
plt.scatter(X[:, 0], X[:, 1], c=y);
plt.xlabel('X1')
plt.ylabel('X2')
plt.xticks([])
plt.yticks([])
