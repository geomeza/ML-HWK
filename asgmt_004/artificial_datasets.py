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
  for point in centerpoints:
    i = centerpoints.index(point)
    if i%2 == 0:
      dataclass = 'x'
    else:
      dataclass = 'o'
    new_cluster = generate_cluster(50, point, dataclass, 1.75)
    complete_dataset.extend(new_cluster)
  return complete_dataset

def split_into_x_y(dataset):
  return [point[:-1] for point in dataset], [point[-1] for point in dataset]
