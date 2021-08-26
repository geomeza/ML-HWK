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

descent_function = lambda a, b: (a)**2 + (a+b-1)**2 + (a+2*b-2)**2

start = time.time()
for i in range(10):
  points = [0,2]
  for i in range(2):
    points = descend(descent_function, points, 0.1, 0.001)
    print(points)

print("Average time in python:", (time.time()-start)/10)
