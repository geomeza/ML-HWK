from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from artificial_datasets import generate_dataset
from artificial_datasets import split_into_x_y

import matplotlib.pyplot as plt
import numpy as np
import random

center_points = [[1,1], [1,3], [3,3], [3,1]]
complete_dataset = generate_dataset(center_points)

x_set, y_set = split_into_x_y(complete_dataset)

rf = RandomForestClassifier(n_estimators = 100)
rf.fit(x_set, y_set)

graph = plt.gca()
for point in complete_dataset:
    if point[2] == 'x':
        color = "bo"
    else:
        color = "ro"
    graph.plot(point[0], point[1], color)

for i in np.arange(-1, 5, 0.1):
    for j in np.arange(-1,5, 0.1):
        prediction = rf.predict([[i,j]])
        if prediction == 'x':
            color = "bo"
        else:
            color = "ro"
        graph.plot(i, j, color, markersize=1)

graph.grid(True)
graph.spines['left'].set_position('zero')
graph.spines['right'].set_color('none')
graph.spines['bottom'].set_position('zero')
graph.spines['top'].set_color('none')
plt.savefig("prediction_space.png")
print("done")