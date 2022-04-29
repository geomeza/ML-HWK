import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import matplotlib as plt

data = pd.read_csv("asgmt_010/practive.csv")

data.columns = ["i", "x", "y"]

data.pop("i")


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
    new_y_data.append([y_arr[i]])
  return np.array(new_x_data), np.array(new_y_data)

x_arr, y_arr = reshape_data(data.x, data.y)

coeffs = LinearRegression().fit(x_arr, y_arr)

y_predictions = [coeffs.predict([x]) for x in x_arr]

print(find_rss(data.x, data.y, y_predictions))