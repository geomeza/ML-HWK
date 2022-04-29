import numpy as np
import math
import sys
sys.path.append('asgmt_001')
from gradient_descent_minimization import descend

x_arr = np.array([[1,1], [1,3], [1,5]])
y_arr = np.array([[4], [16], [25]])


x_inv = np.linalg.pinv(x_arr)
coefficients = np.dot(x_inv, y_arr)
coefficients[0] = math.sqrt(coefficients[1])

print(coefficients)

x_arr = [1,3,5]
y_arr = [2,4,5]

def find_rss(x_arr, y_arr, coefficients):
  rss = 0
  for x in x_arr:
    index = x_arr.index(x)
    rss += (y_arr[index] - coefficients[0] * (x**coefficients[1]))**2
  return rss


print(find_rss(x_arr, y_arr, coefficients))


descent_function = lambda a, b, x: a * (x**b)

derivative_a1 = lambda a,b,x,y: 2 * (math.sqrt(a*x + b) - y) * ((x) / (2 * math.sqrt(a*x + b)))

derivative_b1 = lambda a,b,x,y: 2 * (math.sqrt(a*x + b) - y) * ((1) / (2 * math.sqrt(a*x + b)))

derivative_a2 = lambda a,b,x,y: 2*(a*(b**x)-y)*(b**x)

derivative_b2 = lambda a,b,x,y: 2 * (a*(b**x) - y) * (a*x) * b**(x-1)

def rss_derivative(derivative_a, derivative_b, x_arr, y_arr, points):
  results = [0 for point in points]
  for x in x_arr:
    index = x_arr.index(x)
    y = y_arr[index]
    results[0] += derivative_a(points[0], points[1], x, y)
    results[1] += derivative_b(points[0], points[1], x, y)
  return results

def descend(derivative_a, derivative_b, x_arr, y_arr, points, alpha):
  derivatives = rss_derivative(derivative_a, derivative_b, x_arr, y_arr, points)
  new_points = []
  for i in range(len(points)):
    new_point = points[i] - alpha*derivatives[i]
    new_points.append(new_point)
  return new_points

def descent_for_rss(derivative_a, derivative_b, x_arr, y_arr, points, alpha, old_rss):
  print("old points:", points, "old rss:", find_rss(x_arr, y_arr, points))
  while find_rss(x_arr, y_arr, points) > old_rss:
    points = descend(derivative_a, derivative_b, x_arr, y_arr, points, alpha)
  print("new points:", points, "new rss:", find_rss(x_arr, y_arr, points))
  return "done"

# print(descent_for_rss(derivative_a1, derivative_b1, x_arr, y_arr, coefficients, 0.0001, 4))

# print(descent_for_rss(derivative_a2, derivative_b2, x_arr, y_arr, coefficients, 0.0001, 4))

new_points = descend(derivative_a1, derivative_a2, x_arr, y_arr, [0,1], 0.01)

print(new_points)

print(find_rss(x_arr, y_arr, new_points))