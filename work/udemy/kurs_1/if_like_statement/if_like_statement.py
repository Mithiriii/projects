import os

path = r'c:\temp\mydata.txt'

#os.remove(path)

'''
if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created' % path)
'''

result = os.path.isfile(path) or open(path, 'x').close()
print(result)