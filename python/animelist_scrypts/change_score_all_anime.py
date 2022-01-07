import os
from xml.etree import ElementTree

file_name = "animelist.xml" #important!!!! give your own file name such as animelist_1641543162_-_5339691.xml
full_file = os.path.abspath(os.path.join(file_name)) #The xml file must be in the same folder, if you want you can change it, you have to change this line, but why?

dom = ElementTree.parse(full_file)

courses = dom.findall('anime')

for c in courses:
    a = -1
    my_score = c.find("my_score")
    anime_name = c.find("series_title")
    while a < 0 or a > 10:
        a = input(anime_name.text + ":")
        my_score.text = str(a)   
    update = c.find("update_on_import") 
    update.text = str(1)

dom.write('editing_list.xml')