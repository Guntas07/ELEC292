# Question 1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv(r"C:\Users\gunta\Downloads\heart.csv")
data = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.hist(ax=ax.flatten()[:13])
fig.tight_layout()
plt.show()

# Question 3
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
for i in range(0, 13):
    ax.flatten()[i].hist(data.iloc[:, i])
    ax.flatten()[i].set_title(data.columns[i], fontsize=15)
fig.tight_layout()
plt.show()

# Question 4
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.plot(ax=ax.flatten()[:13], kind='density', subplots=True, sharex=False)
plt.tight_layout()
plt.show()

# Question 5
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.plot(ax=ax.flatten()[:13], kind='box', subplots=True, sharex=False, sharey=False)
plt.tight_layout()
plt.show()

# Question 6
fig, ax = plt.subplots(ncols=13, nrows=13, figsize=(30,30))
pd.plotting.scatter_matrix(data, ax=ax)
plt.tight_layout()
plt.show()

# Question 8
dataset = pd.read_csv(r"C:\Users\gunta\Downloads\winequalityN.csv")

dataset = dataset.iloc[:, 1:]

dataset['quality'] = dataset['quality'].apply(lambda x: 1 if x >= 8 else 0)

X = dataset.drop(columns=['quality'])  # Features
y = dataset['quality']  # Labels

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

colors = np.array(['pink', 'red'])

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=colors[y], alpha=0.5, label="low-quality")
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], c='red', alpha=0.8, label="high-quality")

plt.xlabel("Principal Component - 1")
plt.ylabel("Principal Component - 2")
plt.title("PCA of Wine Quality Dataset")
plt.legend()
plt.show()

# Question 9

pca = PCA(n_components=11)
X_pca = pca.fit_transform(X_scaled)

colors = np.array(['pink', 'red'])

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 7], X_pca[:, 8], c=colors[y], alpha=0.5, label="low-quality")
plt.scatter(X_pca[y == 1, 7], X_pca[y == 1, 8], c='red', alpha=0.8, label="high-quality")

plt.xlabel("Principal Component - 8")
plt.ylabel("Principal Component - 9")
plt.title("PCA of Wine Quality Dataset")
plt.legend()
plt.show()
