import sys
sys.path.append('asgmt_004')
from artificial_datasets import generate_dataset
from artificial_datasets import split_into_x_y

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import numpy as np
import random

center_points = [[1,1], [1,3], [3,3], [3,1]]
complete_dataset = generate_dataset(center_points)

x_set, y_set = split_into_x_y(complete_dataset)

x_train, x_test, y_train, y_test = train_test_split(x_set, y_set, test_size=0.5)


nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3, 3), activation = "logistic", max_iter = 25000, random_state=1)
nn.fit(x_train, y_train)

graph = plt.gca()
for point in complete_dataset:
    if point[2] == 'x':
        color = "bo"
    else:
        color = "ro"
    graph.plot(point[0], point[1], color)

for i in np.arange(-1, 5, 0.1):
    for j in np.arange(-1,5, 0.1):
        prediction = nn.predict([[i,j]])
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
plt.savefig("neural_net_prediction_space.png")
print("done")
