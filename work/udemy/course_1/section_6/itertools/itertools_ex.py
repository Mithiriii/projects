import itertools as it
import math
import operator

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for x in it.permutations(notes, 4):
    print(x)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes)) / math.factorial(len(notes) - 4)))

input('Press enter')

for x in it.product(notes, repeat=4):
    print(x)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
    pow(len(notes), 4)))

