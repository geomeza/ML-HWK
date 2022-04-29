import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPRegressor

data = pd.read_csv("asgmt_010/practive.csv")

data.columns = ["i", "x", "y"]

data.pop("i")

test_data = pd.read_csv("asgmt_010/test.csv")

test_data.columns = ["i", "x", "y"]

test_data.pop("i")

def find_rss(x_arr, y_arr, predictions):
  rss = 0
  x_arr = list(x_arr)
  for x in x_arr:
    index = x_arr.index(x)
    rss += (y_arr[index] - predictions[index])**2
  return rss

def reshape_data(x_arr, y_arr):
  new_x_data = []
  new_y_data = []
  x_arr = list(x_arr)
  y_arr = list(y_arr)
  for i in range(len(x_arr)):
    new_x_data.append([x_arr[i]])
    new_y_data.append(y_arr[i])
  return np.array(new_x_data), np.array(new_y_data)

x_arr, y_arr = reshape_data(data.x, data.y)

test_x_arr, test_y_arr = reshape_data(test_data.x, test_data.y)

regr = MLPRegressor(random_state=1, max_iter=500).fit(x_arr, y_arr)
y_predictions = [regr.predict([x]) for x in test_x_arr]

print("RSS on test dataset:", find_rss(test_data.x, test_data.y, y_predictions))

print("plotting data")
x_arr = [x[0] for x in x_arr]
for i in range(len(x_arr)):
  plt.scatter(x_arr[i],y_arr[i])
x_arr = np.array(x_arr)
x_line_vals = [x.item() for x in np.arange(x_arr.min(), x_arr.max())]
plt.plot(x_line_vals, [regr.predict([[x]]) for x in x_line_vals])
plt.savefig("kaggle_competition.png")

print("DONE!")