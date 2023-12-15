#Practical No.08
#Aim: Feed Forward Back Propagation Neural Network

import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)
np.random.seed(42)
input_size = 2
hidden_size = 3
output_size = 1
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)

bias_hidden = np.zeros((1, hidden_size))
bias_output = np.zeros((1, output_size))
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])


epochs = 10000
learning_rate = 0.1

for epoch in range(epochs):
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    loss = 0.5 * np.mean((predicted_output - y) ** 2)

    
    error = y - predicted_output
    output_delta = error * sigmoid_derivative(predicted_output)

    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_delta) * learning_rate

    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate

test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights_input_hidden) + bias_hidden), weights_hidden_output) + bias_output)

print("Predicted Output after training:")
print(predicted_output)
