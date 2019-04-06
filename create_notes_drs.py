import os

def main():

    print(main)

dirName = 'CyberSecurity-Notes'
try:
    os.mkdir(dirName)
    print("Directory" , dirName , ("Created"))   
except FileExistsError:
    print("Directory" , dirName , ("already exists"))

for i in range(24):
    for x in range(3):
        os.makedirs(os.path.join('CyberSecurity-Notes/Week' + str(i+1) + '' '/Day' + '' +str(x+1)))



    
####
#run the script before checking it 