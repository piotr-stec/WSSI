import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    def __init__(self, n_inputs, bias = 0., weights = None):
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b)


class NeuralNetwork:
    # n_layers - ilość warstw - input_layer -> hidden layers -> output layer
    # n_neurons - ilość neuronów w każdej warstwie
    def __init__(self, n_layers, n_neurons):
        self.layers = []
        self.n_hidden_layers = n_layers-1
        self.n_neurons = n_neurons
        for layer in range(self.n_hidden_layers):
            new_layer = [Neuron(n_neurons[layer]) for _ in range(n_neurons[layer+1])]
            self.layers.append(new_layer)

    def build(self, data):
        for layer in self.layers:
            data = np.array([neuron(data) for neuron in layer])
        return data


n_layers, n_neurons = (4, (3, 4, 4, 1))
nn = NeuralNetwork(n_layers, n_neurons)

inputs = np.array([0.5, -0.2, 0.1])
output = nn.build(inputs)
print(f'Output: {output}')


def draw_neural_net(ax, left, right, bottom, top, layer_sizes):
    # Wyznaczenie odstępów
    v_spacing = (top - bottom) / float(max(layer_sizes))
    h_spacing = (right - left) / float(len(layer_sizes) - 1)

    # Rysowanie neuronów, tła za nimi oraz napisów
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing * (layer_size - 1) / 2. + (top + bottom) / 2.
        # Neurony
        for m in range(layer_size):
            if n == 0:
                circle = plt.Circle((n * h_spacing + left, layer_top - m * v_spacing), v_spacing / 4.,
                                    color='red', ec='k', zorder=4)
                ax.add_artist(circle)
            elif n == len(layer_sizes) - 1:
                circle = plt.Circle((n * h_spacing + left, layer_top - m * v_spacing), v_spacing / 4.,
                                    color='green', ec='k', zorder=4)
                ax.add_artist(circle)
            else:
                circle = plt.Circle((n * h_spacing + left, layer_top - m * v_spacing), v_spacing / 4.,
                                    color='blue', ec='k', zorder=4)
                ax.add_artist(circle)

        # Tło oraz podpisy
        if n == 0:
            background = plt.Rectangle((left / 2, 0),
                                       left, 1, color='pink', zorder=-1)
            ax.add_patch(background)
            ax.text(left / 2 + left / 2, 0, 'Input layer', ha='center', fontsize=12, color='red', weight='bold')

        elif n == len(layer_sizes)-1:
            background = plt.Rectangle((n * h_spacing + left/2, 0), left, 1 ,
                                       color='lightgreen', zorder=-1)
            ax.text(n * h_spacing + left, 0, 'Output layer', ha='center', fontsize=12, color='green', weight='bold')
            ax.add_patch(background)
        else:
            background = plt.Rectangle((n * h_spacing + left/2 , 0), left, 1, color='lightblue', zorder=-1)
            ax.text(n * h_spacing + left, 0, f'Hidden layer {n}', ha='center', fontsize=12, color='blue', weight='bold')
            ax.add_patch(background)

    # Dodanie lini łączących neurony
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing * (layer_size_a - 1) / 2. + (top + bottom) / 2.
        layer_top_b = v_spacing * (layer_size_b - 1) / 2. + (top + bottom) / 2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n * h_spacing + left, (n + 1) * h_spacing + left],
                                  [layer_top_a - m * v_spacing, layer_top_b - o * v_spacing], c='k')
                ax.add_artist(line)


fig = plt.figure(figsize=(12, 12))
ax = fig.gca()
ax.axis('off')
draw_neural_net(ax, .1, .9, .1, .9, n_neurons)
plt.show()
