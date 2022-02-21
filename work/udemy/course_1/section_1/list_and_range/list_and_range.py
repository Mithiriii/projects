for i in range(10, 0, -1):
    print(i)

list = list(range(10))
print('List:', list, type(list), id(list))

list2 = list[:]
print('List:', list2, type(list2), id(list2))

# print(list[-1::-1])