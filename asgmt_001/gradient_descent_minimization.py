import time

def central_difference(function, points, h):
  results = []
  for i in range(len(points)):
    points_forward = [point for point in points]
    points_forward[i] = points_forward[i] + h

    points_backward = [point for point in points]
    points_backward[i] = points_backward[i] - h

    result = (function(*points_forward) - function(*points_backward))/ (2*h)
    results.append(result)
  return results

def descend(function, points, h, alpha):
  derivatives = central_difference(function, points, h)
  new_points = []
  for i in range(len(points)):
    new_point = points[i] - alpha*derivatives[i]
    new_points.append(new_point)
  return new_points

descent_function = lambda x,y: 1 + 2*x**2 + 3*y**2


# start = time.time()
# for i in range(10):
#   first_points = descend(descent_function, [1,2], 0.1, 0.001)
#   print(first_points)
#   second_points = descend(descent_function, first_points, 0.1, 0.001)
#   print(second_points)

# print("Average time in python:", (time.time()-start)/10)
