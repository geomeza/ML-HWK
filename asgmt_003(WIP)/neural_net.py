class Neuron:

  def __init__(self, index, edges, weights):
    self.index   = index
    self.inputs  = [edge[0] for edge in edges if edge[1] == index]
    self.outputs = [edge[1] for edge in edges if edge[0] == index]
    self.weights = {key: val for key,val in weights.items() if index in key}

class NeuralNetwork:

    def __init__(self, inputs, edges, weights, alpha, activation_function, activation_derivative):
        self.alpha                 = alpha
        self.edges                 = edges
        self.points                = inputs
        self.output_node           = max([edge[1] for edge in edges])
        self.weights               = weights
        self.nodes                 = [Neuron(i, self.edges, self.weights) for i in range(self.output_node+ 1)]
        self.activation_function   = activation_function
        self.activation_derivative = activation_derivative
        self.add_bias_node()
        self.get_neuron_values()
        self.get_neuron_gradients()

    def add_bias_node(self):
      self.points = {(a,b,1): self.points[(a,b)] for a,b in self.points.keys()}

    def get_neuron_values(self):
      self.node_input_values = {}
      self.node_output_values = {}
      for i in range(self.output_node + 1):
        neuron = self.nodes[i]
        input_value = sum([self.get_node_value(node) for node in neuron.inputs])
        self.node_input_values[i] = input_value
        self.node_output_values[i] = self.activation_function(input_value)
      
    def get_node_value(self, node_index, inputs):
        input_indexes = [i for i in range(len(inputs))]
        if node_index in input_indexes:
            return self.activation_function(inputs[node_index])
        else:
            node_value = 0
            for input_node in self.get_node_inputs(node_index):
                node_value += self.get_node_value(input_node, inputs) * self.weights[(input_node, node_index)]
            node_value = self.activation_function(node_value)
            return node_value

    def get_activity_gradient(self, node_index, value):
        if (node_index != self.output_node):
            node_outputs = self.nodes[node_index].outputs
            for output_node in node_outputs:
                value *= self.weights[(node_index, output_node)]
                value = self.get_activity_gradient(output_node, value)
        return value

    def error_gradient(self, weight, inputs):
        output_node_value = self.get_node_value(self.output_node, inputs)
        result = 2*output_node_value * self.get_node_value(weight[0], inputs)
        if (weight[1] == self.output_node):
            return result
        else:
            starter_node_outputs = self.nodes[weight[1]].outputs
            for node in starter_node_outputs:
                result *= self.weights[(weight[1], node)]
                self.get_activity_gradient(node, result)
        return result

    def update_weights(self):
        new_weights = {}
        misclassified_points = []
        for point in self.points.keys():
            point_output = self.get_node_value(self.output_node, point)
            if (point_output < 0 and self.points[point] == 1 or point_output > 0 and self.points[point] == -1):
                misclassified_points.append(point)
        for edge in self.edges:
            edge_weight = self.weights[edge]
            whole_gradient = sum([self.error_gradient(edge, point) for point in misclassified_points])
            new_weights[edge] = edge_weight - self.alpha*whole_gradient
        self.weights = new_weights
        return
