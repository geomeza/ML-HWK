from artificial_datasets import generate_dataset
from artificial_datasets import split_into_x_y
import matplotlib.pyplot as plt

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