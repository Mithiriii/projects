import itertools

import itertools as it
import operator

'''
mylist = ['a', 'b', 'c', 'd']

for combination in it.combinations(mylist, 3):
    print(combination)

print("*"*30)

for combination in it.permutations(mylist, 3):
    print(combination)

print("*"*30)

for combination in it.combinations_with_replacement(mylist, 3):
    print(combination)
'''

money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

results = []

for i in range(1, 101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            results.append(combination)

results = set(results)

for results in results:
    print(results)
print("*"*30)
print("*"*30)

money = [50, 20, 10]

for i in range(1, 101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)
print("*"*30)
print("*"*30)
data = [1, 2, 3, 4, 5]
result = it.accumulate(data, operator.mul)
for each in result:
    print(each)

print("*"*30)
print("*"*30)

