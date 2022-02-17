import math


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


#używamy funkcji sigmoid zamiast zwykłego kroku
def sigmoid(t):
    return 1 / (1 + math.exp(-t))


def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))


def feed_forward(neural_network, input_vector):
    outputs = []
    for layer in neural_network:
        input_with_bias = input_vector + [1]    #dodaj wartość progową
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]          #oblicz wartość wyjściową każdego neuronu
        outputs.append(output)
        #wyjście warstwy jest wejściem kolejnej warstwy
        input_vector = output
    return outputs


#PROPAGACJA WSTECZNA

def back_propagate(network, input_vector, target):
    hidden_outputs, outputs = feed_forward(network, input_vector)
    output_deltas = [output * (1 - output) * (output - target[i])
                      for i, output in enumerate(outputs)]

    #dostosuj wagi dla warstwy wyjściowej, przetwarzaj neurony pojedynczo
    for i, output_neuron in enumerate(network[-1]):
        #skupiaj się na i-tym neuronie warstwy wyjściowej
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            #dostosuj j-tą wagę na podstawie parametru delta neuronu i jego i-tego wejścia
            output_neuron[j] -= output_deltas[i] * hidden_output

    #wsteczna propagacja błędów do warstwy ukrytej
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    #dobierz wagi dla warstwy ukrytej, przetwarzaj neurony pojedynczo
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input
