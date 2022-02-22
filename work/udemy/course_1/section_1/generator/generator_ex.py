ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes1 = ((a, b) for a in ports for b in ports)
print(routes1)
i = 0
for x in routes1:
    i=i+1

print(i)

routes2 = ((a, b) for a in ports for b in ports if a != b)
print(routes2)

j = 0
for x in routes2:
    j=j+1

print(j)

routes3 = ((a, b) for a in ports for b in ports if a < b)
print(routes3)

ij = 0
for x in routes3:
    ij=ij+1

print(ij)