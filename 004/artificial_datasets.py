import matplotlib.pyplot as plt
import random

def generate_cluster(num_points, center, dataclass, distance):
  dataset = []
  for i in range(num_points):
    x_val = random.uniform(center[0]- distance, center[0] + distance)
    y_val = random.uniform(center[1]- distance, center[1] + distance)
    dataset.append([x_val, y_val, dataclass])
  return dataset

def generate_dataset(centerpoints):
  complete_dataset = []
  for point in center_points:
    i = center_points.index(point)
    if i%2 == 0:
      dataclass = 'x'
    else:
      dataclass = 'o'
    new_cluster = generate_cluster(50, point, dataclass, 1.75)
    complete_dataset.extend(new_cluster)
  return complete_dataset

center_points = [[1,1], [1,3], [3,3], [3,1]]
complete_dataset = generate_dataset(center_points)

graph = plt.gca()
for point in complete_dataset:
  if point[2] == 'x':
    color = "bo"
  else:
    color = "ro"
  graph.plot(point[0], point[1], color)

graph.grid(True)
graph.spines['left'].set_position('zero')
graph.spines['right'].set_color('none')
graph.spines['bottom'].set_position('zero')
graph.spines['top'].set_color('none')
plt.savefig("artificial_data.png")
print("done")
