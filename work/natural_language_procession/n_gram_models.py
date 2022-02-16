import random
import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def fix_unicode(text):
    return text.replace(u"\u2019", "'")


url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

content = soup.find("div", "entry-content")
regex = r"[\w']+|[\.]"      #wybiera słowa i kropki

document = []

for paragraph in content("p"):
    words = re.findall(regex, fix_unicode(paragraph.text))
    document.extend(words)

bigrams = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in bigrams:
    transitions[prev].append(current)


def generate_using_bigrams(transitions):
    current = "."
    result = []
    while True:
        next_word_candidates = transitions[current]
        current = random.choice(next_word_candidates)
        result.append(current)
        if current == ".":
            return " ".join(result)


print(generate_using_bigrams(transitions))


trigrams = zip(document, document[1:], document[2:])
trigram_transitions = defaultdict(list)
starts = []

for prev, current, next in trigrams:
    if prev == ".":
        starts.append(current)
    trigram_transitions[(prev, current)].append(next)


def generate_using_trigrams(starts, trigram_transitions):
    current = random.choice(starts)
    prev = "."
    result = [current]
    while True:
        next_word_candidates = trigram_transitions[(prev, current)]
        next = random.choice(next_word_candidates)

        prev, current = current, next
        result.append(current)

        if current == ".":
            return " ".join(result)


print(generate_using_trigrams(starts, trigram_transitions))


