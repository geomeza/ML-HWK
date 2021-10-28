from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from artificial_datasets import generate_dataset
from artificial_datasets import split_into_x_y

import matplotlib.pyplot as plt
import random

center_points = [[1,1], [1,3], [3,3], [3,1]]
complete_dataset = generate_dataset(center_points)

x_set, y_set = split_into_x_y(complete_dataset)

x_train, x_test, y_train, y_test = train_test_split(x_set, y_set, test_size=0.5)

scores = {}

for k in range(1,50):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores[k] = accuracy_score(y_test, y_pred)

plt.plot(list(scores.keys()), list(scores.values()))
plt.grid(True)
plt.savefig("knn_test.png")
plt.clf()
scores = {}

for split in range(2,50):
    dt = DecisionTreeClassifier(min_samples_split=split)
    dt.fit(x_train, y_train)
    y_pred = dt.predict(x_test)
    scores[split] = accuracy_score(y_test, y_pred)

plt.plot(list(scores.keys()), list(scores.values()))
plt.grid(True)
plt.savefig("decision_tree_test.png")
plt.clf()
scores = {}

for trees in range(1,100):
    rf = RandomForestClassifier(n_estimators=trees)
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)
    scores[trees] = accuracy_score(y_test, y_pred)

plt.plot(list(scores.keys()), list(scores.values()))
plt.grid(True)
plt.savefig("random_forest_test.png")

print("done")