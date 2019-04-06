import os

import shutil

def pptx_copy():
    my_path = os.path.expanduser("~/Downloads")
    directory = os.listdir(my_path)
    destination = os.getcwd()

    for x in directory:
        if x.endswith(".ppt") or x.endswith(".pptx"):
            print(x) 
            your_path = os.path.join(my_path, x)
            shutil.copy(your_path, destination)
            print(your_path)
    

pptx_copy()


    