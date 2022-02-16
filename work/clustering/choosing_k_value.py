from k_means import KMeans


def squared_distance(v, w):
    return sum_of_squares(vector_substract(v, w))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def squared_clustering_errors(inputs, k):
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)

    return sum(squared_distance(input, means[cluster])
               for input, cluster in zip(inputs, assignments))


