import numpy as np
import matplotlib as plt
import math

class PrincinpalComponents:

  def __init__(self):
    self.data = None
    self.num_components = None
    self.data_columns = None
    self.eigen_values = []
    self.eigen_vectors = []
    self.transformed_data = []

  def sort_eigen_info(self, values, vectors):
    sorted_info = sorted([(values[i],vectors[i]) for i in range(self.num_components)])
    return [sorted_info[i][0] for i in range(len(sorted_info))], [sorted_info[i][1] for i in range(len(sorted_info))]

  def fix_correlation_matrix(self, matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if math.isnan(matrix[i][j]):
          matrix[i][j] = 0.01
    return matrix

  def fit(self, data, n = None):
    self.data = data
    self.num_components = len(data[0])
    self.data_columns = np.array(data)
    correlation_matrix = np.corrcoef(self.data_columns.T)
    correlation_matrix = self.fix_correlation_matrix(correlation_matrix)
    eigen_info = np.linalg.eig(correlation_matrix)
    self.eigen_values, self.eigen_vectors = self.sort_eigen_info(eigen_info[0], eigen_info[1])
    self.transformed_data = np.array([self.transform(point, n) for point in data])
    print("transformed data")

  def transform(self, point, n = None):
    if n is None:
      n = self.num_components
    transformed_point = []
    for i in range(n):
      vector = self.eigen_vectors[i]
      transformed_point.append(sum(point[x]*vector[x] for x in range(self.num_components)))
    return np.array(transformed_point)
