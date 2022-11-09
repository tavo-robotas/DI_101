import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model

pts = np.loadtxt('../data_samples/linpts_smaller.txt')
X = pts[:,:2]
Y = pts[:,2].astype('int')
clf = sklearn.linear_model.LinearRegression()
clf.fit(X, Y)
b = clf.intercept_
w1, w2 = clf.coef_.T
c = -b/w2 + 0.5
m = -w1/w2
xmin, xmax = -1, 2
ymin, ymax = -1, 2.5
xd = np.array([xmin, xmax])
yd = m*xd + c
plt.figure(figsize=(16,8))
plt.plot(xd, yd, 'k', lw=2)
plt.fill_between(xd, yd, ymin, color='tab:red', alpha=0.55)
plt.fill_between(xd, yd, ymax, color='tab:blue', alpha=0.55)
plt.scatter(*X[Y==0].T, c='g', s=150)
plt.scatter(*X[Y==1].T, c='b',s=150)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.tight_layout()
plt.xticks([])
plt.yticks([]);