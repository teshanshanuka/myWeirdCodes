import os
from shutil import move

print("This will move all given type of files in the folders here (NOT SUBFOLDERS) to '.'")

folders = [item for item in os.listdir() if os.path.isdir(item)]

files = {folder : os.listdir(folder) for folder in folders}

filetypes = input("Enter filetypes you want to move out (.mkv,.srt):\t")

def is_type(filename, filetypes):
    filetypes = filetypes.split(',')
    for typ in filetypes:
        if filename.endswith(typ):
            return True
    return False

for folder in files:
    for f in files[folder]:
        if is_type(f, filetypes):
            print(move(os.path.join(folder,f), '.'))

input('Done! Press enter to continue')
