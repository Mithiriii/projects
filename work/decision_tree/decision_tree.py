import math
from collections import Counter, defaultdict
from functools import partial


#mechanizma określania entropii
#entropia - miara niepewności
def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)


def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]


def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)


def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


#dane wejsciowe
inputs = [
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)
]


#szukamy podziału o najmniejszej entropii
#funkcja przeprowadzająca podział
def partition_by(inputs, attribute):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]   #określa wartość wybranego atrybutu
        groups[key].append(input)   #dodaj te dane wejściowe do właściwej listy
    return groups


#funkcja obliczjąca entropię
def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())


for key in ['level', 'lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(inputs, key))

#najniższą entropię uzyskuje się w wyniku podziału atrybutu level
#należy więc utworzyć poddrzewo dla każdej możliwej wartości tego atrybutu

senior_inputs = [(input, label)
                 for input, label in inputs if input["level"] == "Senior"]
print("\n")
for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(senior_inputs, key))

#dla tweets wyszła entropia 0, więc jeżeli senior + tweets = true to senior - tweets = false

junior_inputs = [(input, label)
                 for input, label in inputs if input['level'] == "Junior"]

print("\n")
for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(junior_inputs, key))


#funkcja klasyfikująca dane wejściowe
def classify(tree, input):
    #jeżeli to węzeł końcowy zwróć jego wartość
    if tree in [True, False]:
        return tree

    attribute, subtree_dict = tree
    subtree_key = input.get(attribute)
    if subtree_key not in subtree_dict:     #warunek określający co się stanie jeżeli nie uwzględnimy jakiegoś poddrzewa
        subtree_key = None

    subtree = subtree_dict[subtree_key]
    return classify(subtree, input)


#funkcja budująca reprezentacje drzewa na podstawie treningowego zbioru danych
def build_tree_id3(inputs, split_candidates=None):
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues

    if not split_candidates:
        return num_trues >= num_falses

    best_attribute = min(split_candidates,
                         key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates if a != best_attribute]

    subtrees = {attribute: build_tree_id3(subset, new_candidates)
                 for attribute, subset in iter(partitions.items())}

    subtrees[None] = num_trues > num_falses

    return best_attribute, subtrees


tree = build_tree_id3(inputs)

temp = classify(tree, { "level" : "Junior",
                        "lang": "Java",
                        "tweets": "yes",
                        "phd": "no"})
print(temp)


#LASY LOSOWE
#drzewa decyzyjne mają tendencję do przeuczenia dlatego tworzy się lasy losowe
def forest_classify(trees, input):
    votes = [classify(tree, input) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]

# Przyjrzyj się wszystkim kandydatom do podziału, jeżeli jest ich odpowiednio mało.
#if len(split_candidates) <= self.num_split_candidates:
# sampled_split_candidates = split_candidates

# W przeciwnym wypadku wylosuj próbkę kandydatów.
#else:
# sampled_split_candidates = random.sample(split_candidates,
# self.num_split_candidates)
# Wybierz najlepszy atrybut z wybranej próbki kandydatów.
#best_attribute = min(sampled_split_candidates,
# key=partial(partition_entropy_by, inputs))
#partitions = partition_by(inputs, best_attribute)
