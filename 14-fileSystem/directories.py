import os, shutil

# create folder
if not os.path.isdir("./my-folder"):
    os.mkdir("./my-folder")
else:
    print("The folder 'my-folder' already exists")

# delete folder
os.rmdir("./my-folder")

# copy folder
original_Path = "./my-folder"
new_Path = "./my-folder (copied)"
shutil.copytree(original_Path, new_Path)

# show folder content
content = os.listdir("./my-folder")

for file in content:
    print(f"File: {file}")