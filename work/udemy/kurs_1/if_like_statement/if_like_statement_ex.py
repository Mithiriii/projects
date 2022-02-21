import os

path = r'c:\temp\mydata.txt'


def count_word(path):
    file = open(path, 'r')
    var = file.read()
    list = var.split(' ')
    return len(list)


if os.path.isfile(path):
    x = count_word(path)
    print(x)
else:
    print("file not exist")