import os
from xml.etree import ElementTree

file_name = "animelist.xml"
full_file = os.path.abspath(os.path.join(file_name)) 

dom = ElementTree.parse(full_file)

courses = dom.findall('anime')

for c in courses:
    
    my_score = c.find("my_score")
    a = int(my_score.text)
    if(a>0):
        a = a-1 
        my_score.text = str(a)
   
    update = c.find("update_on_import") 
    update.text = str(1)

dom.write('editing_list.xml')