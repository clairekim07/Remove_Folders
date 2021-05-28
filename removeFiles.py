import time
import os
import shutil

path = input("Enter the path of the folder you want to remove: ")
days = 30
seconds = time.time()-(days*24*60*60)
if os.path.exists(path) is True:
    for root_folder, folders, files in os.walk(path):
        if seconds>= getFolderAge(root_folder):
            removeFolder(root_folder)

        else:
            
            if seconds >= getFolderAge(folders):
                removeFolder(folders)

            if seconds >= getFolderAge(files):
                removeFile(files)
            
            
else:
    print("Path/Folder not found")

def getFolderAge(path):
    folderAge = os.stat(path).st_mtime
    return folderAge

def removeFile(file):
    joinedFilePath = os.path.join(path+'/'+file)
    if not os.remove(joinedPath):
        print("File removed succesfully")
    else:
        print("File was not deleted.")
def removeFolder(folder):
    joinedFolderPath = os.path.join(path+'/'+folder)
    if not shutil.rmtree(joinedFolderPath):
        print("File removed succesfully")
    else:
        print("File was not deleted.")