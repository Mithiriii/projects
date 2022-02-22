import os

files_to_process= [
    r"D:\projects\work\udemy\course_1\section_1\expr\file_1.py",
    r"D:\projects\work\udemy\course_1\section_1\expr\file_2.py"
]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)