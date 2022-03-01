a_tuple = (1, 2, 3, 4, 5)

for x in a_tuple:
    print(x)

# print(next(a_tuple))

it = iter(a_tuple)
print("*"*30)

print(next(it))
print(next(it))
print(next(it))
print("*"*30)

a_list = [1, 2, 3, 4, 5]
print("*"*30)

for i in a_list:
    print(i)
print("*"*30)

it_l = iter(a_list)
print(next(it_l))
print(next(it_l))
print(next(it_l))

a_set = {1, 2, (3, 4), 'another element', 3, 4}