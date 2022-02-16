def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


#Percepton składa się z pojedyńczego neuronu z n wejściami binarnymi, oblicza sumę ważoną danych wejściowych i
#generuje wartość wyjściową określającą czy suma wazona jest zerowa czy uzyskała wyższą wartość
def step_function(x):
    return 1 if x >= 0 else 0


def perceptron_output(weights, bias, x):    #weights - wagi, bias - wartość progową
    calculation = dot(weights, x) + bias
    return step_function(calculation)