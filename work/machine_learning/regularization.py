#Regularyzacja jest techniką polegającą na dodawaniu do czynnika błędu kary, która jest zwiększana wraz ze wzrostem wartości beta.
#Następnie próbujemy zminimalizować sumę błędów i kar.


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def ridge_penalty(beta, alpha):
    return alpha * dot(beta[1:], beta[1:])