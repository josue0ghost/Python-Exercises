from io import open
import pathlib
import shutil

# create file on folder
path = str(pathlib.Path().absolute()) + "/text.txt"
print(path)
file = open(path, "a+")

# write on file
file.write("Hi!\n")
file.close()

readedFile = open(path, "r") # r for read permissions
# content = readedFile.read()
# print(content)

# save content on list
contentList = readedFile.readlines()
readedFile.close()

print(contentList)

# copy file
srcPath = path
newPath = str(pathlib.Path().absolute()) + "/text-copied.txt"
shutil.copyfile(srcPath, newPath)

# move file
# shutil.move(srcPath, newPath)

# Delete file
"""
    import os
    os.remove(path)
"""

# A file exists?
"""
    import os.path
    print(os.path.abspath("./"))
    if os.path.isfile(os.path.abspath("./") + "/text.txt"):
        print("File exists")
    elif:
        print("File does not exists")
"""