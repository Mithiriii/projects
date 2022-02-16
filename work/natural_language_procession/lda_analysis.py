import random
from collections import Counter


#funkcja losująca indeks na podstawie dowolnego zestawu wag
def sample_from(weights):
    total = sum(weights)
    rnd = total * random.random()
    for i, w in enumerate(weights):
        rnd -= w
        if rnd <= 0:
            return i


documents = [
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

#liczba unikalnych słów:
distinct_words = set(word for document in documents for word in document)
W = len(distinct_words)

#Liczba dokumentów
K = len(documents)



#lista liczników, po jednym dla każdego dokumentu
document_topic_counts = [Counter() for _ in documents]

#lista liczników, po jednym dla każdego tematu
topic_word_counts = [Counter() for _ in range(K)]

#lista liczb, po jednej dla każdego tematu
topic_counts = [0 for _ in range(K)]

#lista liczb, po jednej dla każdego tematu
document_lengths = map(len, documents)



def p_topic_given_document(topic, d, alpha=0.1):
    return (document_topic_counts[d][topic] + alpha) / (document_lengths[d] + K * alpha)


def p_word_given_topic(word, topic, beta=0.1):
    return (topic_word_counts[topic][word] + beta) / (topic_counts[topic] + W * beta)


def topic_weight(d, word, k):
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)


def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])

