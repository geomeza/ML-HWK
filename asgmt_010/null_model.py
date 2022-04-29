import pandas as pd
import numpy as np
import sklearn
import math
import matplotlib as plt

data = pd.read_csv("asgmt_010/practive.csv")

data.columns = ["i", "x", "y"]

data.pop("i")
print(data)


def find_rss(x_arr, y_arr, predictions):
  rss = 0
  x_arr = list(x_arr)
  for x in x_arr:
    index = x_arr.index(x)
    rss += (y_arr[index] - predictions[index])**2
  return rss


def null_model_fit(x_arr):
  return [0 for x in x_arr]


print(find_rss(data.x, data.y, null_model_fit(data.x)))
