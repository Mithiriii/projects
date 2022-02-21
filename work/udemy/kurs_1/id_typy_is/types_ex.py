a = 10
b = a
c = b

print(a, b, c)
print(id(a), id(b), id(c))

a = 20

print(a, b, c)
print(id(a), id(b), id(c))

aa = [1, 2, 3]
bb = aa
cc = bb

print(aa, bb, cc)
print(id(aa), id(bb), id(cc))

aa.append(4)
print(aa, bb, cc)
print(id(aa), id(bb), id(cc))

x = 10
y = 10
print(id(x), id(y))

y = y + 1 - 1
y = y + 1
y = y - 1
print(id(x), id(y))

y = y + 1234567890
y = y - 1234567890
print(id(x), id(y))