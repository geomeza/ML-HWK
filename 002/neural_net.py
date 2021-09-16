class NeuralNetwork:

    def __init__(self, inputs, edges, weights, alpha):
        self.alpha        = alpha
        self.edges        = edges
        self.points       = inputs
        self.output_node  = max([edge[1] for edge in edges])
        self.weights      = weights

    def get_node_value(self, node_index, inputs):
        input_indexes = [i for i in range(len(inputs))]
        if node_index in input_indexes:
            return inputs[node_index]
        else:
            node_value = 0
            for input_node in self.get_node_inputs(node_index):
                node_value += self.get_node_value(input_node, inputs) * self.weights[(input_node, node_index)]
            return node_value

    def get_node_inputs(self, node_index):
        return [edge[0] for edge in self.edges if edge[1] == node_index]

    def get_node_outputs(self, node_index):
        return [edge[1] for edge in self.edges if edge[0] == node_index]

    def get_activity_gradient(self, node_index, value):
        if (node_index != self.output_node):
            node_outputs = self.get_node_outputs(node_index)
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
            starter_node_outputs = self.get_node_outputs(weight[1])
            for node in starter_node_outputs:
                result *= self.weights[(weight[1], node)]
                self.get_activity_gradient(node, result)
        return result

    def update_weights(self):
        new_weights = {edge: 0 for edge in self.edges}
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
