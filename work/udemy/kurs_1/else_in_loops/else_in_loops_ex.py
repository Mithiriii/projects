import os
import urllib.request as ur

data_dir = r'c:\temp'
pages = [
    {'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
]

for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
        ur.urlretrieve(page["url"], path)
    except:
        break
else:
    print('All pages download')