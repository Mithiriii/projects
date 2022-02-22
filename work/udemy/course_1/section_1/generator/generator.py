listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []
for a in listA:
    for b in listB:
        product.append((a, b))

print(product)

product = [(a, b) for a in listA for b in listB]
print(product)

product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

product = {a: b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)

print('-'*30)
for x in gen:
    print(x)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("all values have been generated")
        break
