import random
import numpy as np
import matplotlib.pyplot as plt

class Node:

    def __init__(self, act_function, index):
        self.index = index
        self.act_function = act_function
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

class Graph:

    def __init__(self, edges, act_function, mutation_rate, weights = None):
        self.edges = edges
        self.nodes = []
        self.bias_nodes = []
        self.act_function = act_function
        self.mut_rate = mutation_rate
        if weights is None:
            self.weights = {edge: random.uniform(-0.2, 0.2) for edge in edges}
        else:
            self.weights = weights
        self.build_graph()
        self.output_node = self.nodes[-1]

    def make_nodes(self):
        all_nodes = list(set(sum(edges,())))
        for node_index in all_nodes:
            new_node = Node(self.act_function, node_index)
            self.nodes.append(new_node)

    def build_graph(self):
        self.make_nodes()
        for edge in self.edges:
            self.nodes[edge[0]].add_child(self.nodes[edge[1]])
        for node in self.nodes:
            if node.parents == [] and node.index != 0:
                self.bias_nodes.append(node)

    def node_outut(self, node, input):
        if node.index == 0:
            return self.act_function(input)
        elif node in self.bias_nodes:
            return 1
        else:
            node_inputs = [self.weights[(parent.index, node.index)] * self.node_outut(parent, input) for parent in node.parents]
            return self.act_function(sum(node_inputs))
        raise Exception("literally impossible")

def generate_network_edges(layers):
    edges = []

    for depth in range(len(layers)-1):
        stagger1 = sum([layers[k] for k in range(depth)])+(depth)
        stagger2 = sum([layers[k] for k in range(depth+1)])+((depth+1))
        for i in range(layers[depth]+1):
            for j in range(layers[depth+1]):
                edges.append((stagger1+i,stagger2+j))
    return edges

def wacky_mut_rate(): ## I hate this function
    x = (np.random.normal())/((2**(0.5)) * (len(edges)**(0.25)))
    return np.exp(x)

def find_rss(points, network):
    sum = 0
    for point in points:
        sum += (point[1] - network.node_outut(network.output_node, point[0]))**2
    return sum


data = [(0.0 , 7) , (0.2 , 5.6) , (0.4 , 3.56) , (0.6 , 1.23) , (0.8 , -1.03) ,
 (1.0 , -2.89) , (1.2 , -4.06) , (1.4 , -4.39) , (1.6 , -3.88) , (1.8 , -2.64) ,
 (2.0 , -0.92) , (2.2 , 0.95) , (2.4 , 2.63) , (2.6 , 3.79) , (2.8 , 4.22) ,
 (3.0 , 3.8) , (3.2 , 2.56) , (3.4 , 0.68) , (3.6 , -1.58) , (3.8 , -3.84) ,
 (4.0 , -5.76) , (4.2 , -7.01) , (4.4 , -7.38) , (4.6 , -6.76) , (4.8 , -5.22) ]

x_vals = [point[0] for point in data]
y_vals = [point[1] for point in data]

x_min = min(x_vals)
x_max = max(x_vals)

normalized_x = [(x - x_min)/(x_max - x_min) for x in x_vals]

y_max = max(y_vals)
y_min = min(y_vals)
normalized_y = [((2*(y - y_min))/((y_max - y_min)))-1 for y in y_vals]

normalized_points = [(x,y) for x,y in zip(normalized_x, normalized_y)]

edges = generate_network_edges([1,10,6,3,1])
tanh = np.tanh
mut_rate = 0.05

nets = [Graph(edges, tanh, mut_rate) for _ in range(30)]

total_avgs = []
generation = []

print("starting generation making")

for i in range(500):
    print(i, " generation")
    nets_rss = []

    for net in nets:
        nets_rss.append(find_rss(normalized_points, net))
    total_avgs.append(sum(nets_rss)/ len(nets_rss))
    generation.append(i)

    top_15 = sorted(nets, key = lambda n: find_rss(normalized_points, n))[:15]

    children = [Graph(edges, tanh, parent.mut_rate * wacky_mut_rate(), {edge: parent.weights[edge] + parent.mut_rate*(np.random.normal()) for edge in edges}) for parent in top_15]
    nets = top_15 + children
    if i == 0 or i == 499:
        if i == 0:
            print("making first regression curve")
        if i == 499:
            print("making final regression curve")
        graph_fig = plt.gca()
        for point in normalized_points:
            graph_fig.plot(point[0], point[1], "ro")
        for net in nets:
            plt.plot([point[0] for point in normalized_points], [net.node_outut(net.output_node, point[0]) for point in normalized_points])
        if i == 0:
            plt.savefig("first_regression_curve.png")
            plt.clf()
            print("first regression curve done!")
        if i == 499:
            plt.savefig("final_regression_curve.png")
            plt.clf()
            print("final regression curve done!")


print("starting plot")
plt.clf()
graph_fig = plt.gca()
plt.plot(generation, total_avgs)
plt.title("AVG RSS PER GEN")
plt.savefig("avg_rss.png")

plt.clf()
print("regression curve_first_gen")
print("DONE!")