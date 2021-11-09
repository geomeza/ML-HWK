from neural_net import NeuralNetwork

points = {
    (2,1): -1,
    (4,1): -1,
    (3,2): -1,
    (1,2): 1,
    (2,2): 1,
    (1,4): 1
}

edges = [(0,2),(0,3),(1,2),(1,3),(3,4),(2,4)]

weights = {(3,4):-0.1,(2,4):0.2,(1,3):-0.3,(0,3):0.4,(1,2):-0.5,(0,2):0.6}

nn = NeuralNetwork(points, edges, weights, 0.001)

i = 0
while(True):
    i += 1
    old_weights = {key:val for key, val in nn.weights.items()}
    if i in [1,2]:
        print(nn.weights)
    nn.update_weights()
    if (i % 1000 == 0):
        print("-------------------")
        print(i)
        print(nn.weights)
        print("-------------------")
    if (old_weights == nn.weights):
        print(i)
        break