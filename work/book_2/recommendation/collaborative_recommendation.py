import math
from collections import Counter, defaultdict


users_interests = [
        ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
        ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
        ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
        ["R", "Python", "statistics", "regression", "probability"],
        ["machine learning", "regression", "decision trees", "libsvm"],
        ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
        ["statistics", "probability", "mathematics", "theory"],
        ["machine learning", "scikit-learn", "Mahout", "neural networks"],
        ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
        ["Hadoop", "Java", "MapReduce", "Big Data"],
        ["statistics", "R", "statsmodels"],
        ["C++", "deep learning", "artificial intelligence", "probability"],
        ["pandas", "R", "Python"],
        ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
        ["libsvm", "regression", "support vector machines"]
]


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def star(f):
  return lambda args: f(*args)




#metryka podobieństwa kosinusowego
def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))


unique_interests = sorted(list({ interest
                                 for user_interests in users_interests
                                 for interest in user_interests}))


def make_user_interest_vector(user_interests):
    return [1 if interest in user_interests else 0
            for interest in unique_interests]


user_interests_matrix = map(make_user_interest_vector, users_interests)

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interests_matrix]
                     for interest_vector_i in user_interests_matrix]


def most_similar_user_to(user_id):
    pairs = [(other_user_id, similarity)
             for other_user_id, similarity in
             enumerate(user_similarities[user_id])
             if user_id != other_user_id and similarity > 0]
    return sorted(pairs,
                  key=star(lambda _, similarity: similarity), reverse=True)


def user_based_suggestions(user_id, include_current_interests=False):
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_user_to(user_id):
        for interest in users_interests[other_user_id]:
            suggestions[interest] += similarity

    #zamień podobieństwa na posortowaną listę
    suggestions = sorted(suggestions.items(),
                         key=star(lambda _, weight: weight), reverse=True)

    #usuń bierzące zainteresowania
    if include_current_interests:
        return suggestions
    else:
        return [(suggestions, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]

print(user_based_suggestions(0))