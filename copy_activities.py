import os

import shutil 

def stu_activities():
    my_path = os.path.expanduser("~/Downloads")
    directory = os.listdir(my_path)
    destination = os.getcwd()

    for x in directory:
        print(x)
        if x.__contains__("Stu_"):

            your_path = os.path.join(my_path, x)
            shutil.copy(your_path, destination)
            print(your_path)

stu_activities()



