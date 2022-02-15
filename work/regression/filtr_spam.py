import glob, re
import random
from naive_bayes_classifier import NaiveBayesClassifier
from collections import Counter

path = "./spam/*/*/"
data = []


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


#glob.glob zwraca nazwę pliku znajdującego się w podanej ścieżce
for fn in glob.glob(path):
    is_spam = "ham" not in fn
    with open(fn, 'r') as file:
        for line in file:
            if line.startswith("Subject:"):
                #usuwa pierwsze słowo subject i pozostawia resztę
                subject = re.sub(r"^Subject: ", "", line).strip()
                data.append((subject, is_spam))

random.seed(0)
train_data, test_data = split_data(data, 0.75)

classifier = NaiveBayesClassifier()
classifier.train(train_data)

classified = [(subject, is_spam, classifier.classify(subject))
              for subject, is_spam in test_data]

#zakładamy, że spam_probability > 0.5 oznacza, że wiadomość jest spamem
counts = Counter((is_spam, spam_probability > 0.5)
                 for _, is_spam, spam_probability in classified)
print(counts)
