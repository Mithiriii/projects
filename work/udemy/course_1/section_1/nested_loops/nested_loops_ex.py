ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes1 = [(a, b) for a in ports for b in ports]
print(routes1)

routes2 = [(a, b) for a in ports for b in ports if a != b]
print(routes2)

routes3 = [(a, b) for a in ports for b in ports if a < b]
print(routes3)

print(len(routes1))
print(len(routes2))
print(len(routes3))