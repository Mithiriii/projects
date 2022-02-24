text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

f = lambda x: len(x)
print(f(text_list[2]))

le = list(map(lambda x: len(x), text_list))
print(le)
