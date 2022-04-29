import numpy as np
import math
np.set_printoptions(suppress=True)


class Simplex:

  def __init__(self, coeff_matrix):
    self.coeff_matrix = coeff_matrix
    self.num_pivots = len(coeff_matrix[0])
    self.complete_simplex_method()

  def complete_simplex_method(self):
    const_column = self.get_and_remove_constant_column()
    numpy_coeffs = np.array(self.coeff_matrix)
    identity = np.identity(len(self.coeff_matrix) - 1)
    zero_row = [0 for _ in range(len(self.coeff_matrix) - 1)]
    identity = np.append(identity, [zero_row], axis = 0)
    complete_matrix = np.append(numpy_coeffs, identity, axis = 1)
    complete_matrix = np.append(complete_matrix, const_column, axis = 1)
    self.coeff_matrix = [[round(row[i], 2) for i in range(len(row))] for row in complete_matrix]
    self.max_eqn = complete_matrix[-1]
    while not self.check_if_neg(complete_matrix[-1]):
      highest_coeff_index = self.get_highest_coeff_in_max_eqn()
      smallest_ratio = self.get_smallest_ratio_in_matr(highest_coeff_index)
      complete_matrix[smallest_ratio] = complete_matrix[smallest_ratio]/complete_matrix[smallest_ratio][highest_coeff_index]
      for i in range(len(complete_matrix - 1)):
        if i != smallest_ratio:
          multiple = complete_matrix[i][highest_coeff_index]
          complete_matrix[i] = complete_matrix[i] - (multiple * complete_matrix[smallest_ratio])
      self.coeff_matrix = [[round(row[i], 2) for i in range(len(row))] for row in complete_matrix]
    self.max_value = -1*complete_matrix[-1][-1]
    print(self.max_value)

  def check_if_neg(self, row):
    for val in row:
      if val > 0:
        return False
    return True

  def get_and_remove_constant_column(self):
    const_arr = []
    for row in self.coeff_matrix:
      const_arr.append([row[self.num_pivots-1]])
    self.coeff_matrix = [row[:-1] for row in self.coeff_matrix]
    return const_arr

  def get_highest_coeff_in_max_eqn(self):
    not_np_arr = [num for num in self.max_eqn]
    return not_np_arr.index(max(not_np_arr))

  def get_smallest_ratio_in_matr(self, coeff_index):
    ratios = []
    for i in range(len(self.coeff_matrix) - 1):
      ratio = self.coeff_matrix[i][-1]/ self.coeff_matrix[i][coeff_index]
      ratios.append(ratio)
    return ratios.index(min([num for num in ratios if num > 0]))

coeff_matrix = [[2,1,0,10], [1,2,-2,20], [0,1,2,5], [2,-1,2,0]]
simplex_test = Simplex(coeff_matrix)
