from collections import Counter
import math


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    return magnitude(vector_substract(v, w))


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])


def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points, key=lambda point: distance(point, new_point))
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)
