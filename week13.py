import os


# Get path from user, if path not specified, will default to current working directory
path = input('Enter a file path? ')
if path =='':
    path = os.getcwd()
else: 
    path = path  


# Uses listdir method to list all files/directories in specified variable path 
dirs = os.listdir(path)


# Created an empty list
mylist = []


# Prints the contents of the file and directory along with their size
for filename in dirs:
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        mydict ={"path": path+'/'+filename, "size": size}
    else:
        mydict ={"path": path+'/'+filename, "size": "Directory"}
    mylist.append(mydict)
# Print each dictionary in the list
for item in mylist:
    print(item)

