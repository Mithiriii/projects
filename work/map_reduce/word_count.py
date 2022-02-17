from collections import Counter, defaultdict
from tokenize import tokenize
from functools import partial


def word_count_old(documents):
    return Counter(word
                   for document in documents
                   for word in tokenize(document))


def wc_mapper(document):
    for word in tokenize(document):
        yield word, 1


def wc_reducer(word, counts):
    yield word, sum(counts)


#liczenie słów występujących w dokumencie wejściowym za pomocą MapReduce
def word_count(documents):
    collector = defaultdict(list)

    for document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)

    return [output
            for word, counts in collector.iteritems()
            for output in wc_reducer(word, counts)]


#algorytm w ujęciu ogólnym
def map_reduce(inputs, mapper, reducer):
    collector = defaultdict(list)
    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)

    return [output
            for key, values in iter(collector.items())
            for output in reducer(key, values)]


def reduce_values_using(aggregation_fn, key, values):
    yield key, aggregation_fn(values)


def values_reducer(aggregation_fn):
    return partial(reduce_values_using, aggregation_fn)

