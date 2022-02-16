import math


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    return magnitude(vector_substract(v, w))


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


#budowa klastrów od dołu do góry jest alternatywnym sposobem grupowania

leaf1 = ([10, 20],)
leaf2 = ([30, -15],)
merged = (1, [leaf1, leaf2])


def is_leaf(cluster):
    return len(cluster) == 1


def get_children(cluster):
    if is_leaf(cluster):
        raise TypeError("Brak grup potomnych")
    else:
        return cluster[1]


def get_values(cluster):
    if is_leaf(cluster):
        return cluster
    else:
        return [value
                for child in get_children(cluster)
                for value in get_values(child)]


def cluster_distance(cluster1, cluster2, distance_agg=min):
    return distance_agg([distance(input1, input2)
                         for input1 in get_values(cluster1)
                         for input2 in get_values(cluster2)])


def get_merge_order(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]


def star(f):
    return lambda args: f(*args)


def bottom_up_cluster(inputs, distance_agg=min):
    #zacznij od utworzenia jednoelementowych krotek
    clusters = [(input,) for input in inputs]
    #dopóki został więcej niż 1 klaster
    while len(clusters) > 1:
        #znajdź dwa najbliższe klastry
        c1, c2 = min([(cluster1, cluster2)
                      for i, cluster1 in enumerate(clusters)
                      for cluster2 in clusters[:i]],
                     key=star(lambda x, y: cluster_distance(x, y, distance_agg)))
        #usuń je z listy klastrów
        clusters = [c for c in clusters if c != c1 and c != c2]

        #połącz klastry
        merged_cluster = (len(clusters), [c1, c2])

        #dodaj informację o ich połączeniu
        clusters.append(merged_cluster)
    return clusters[0]
