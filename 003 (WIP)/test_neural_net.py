from neural_net import NeuralNetwork

points = {
    (0,3): 1,
    (2,3): 1,
    (2,1): -1,
    (0,1): -1
}

edges = [(0,3),(1,3),(2,3)]

weights = {(0,3): -1, (1,3): 1, (2,3): 0}

nn = NeuralNetwork(points, edges, weights, 0.001, lambda x: x**2, lambda x: 2*x)


nn.update_weights()
print("weights after 1 update:")
print(nn.weights)
