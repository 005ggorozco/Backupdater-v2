# Backupdater v2 by Gabriel Orozco
# Created on April 4, 2026

# libraries
import os

# Path of the folder to be backed up
original = "original" 
backup = "backup"

# List files of a directory method
def listDir(path):

    fileList = []
    
    for root, subroot, files in os.walk(path):

        # Iterate through file list from os.walk()
        for f in files:
            # Join root and file path and add to fileList[]
            fileList.append(os.path.join(root, f))

    return fileList

# End of listDir method

# Compare files between two directories method
def compareDir(list1, list2):
    # Remove elements present in 'backup' that are not present in 'original'
    # before comparing both lists

    # Iterate through a copy
    for i in list2[:]:

        # Get only the file name
        i = i[ (i.rfind("\\") + 1) : ] # rfind() - find last occurence of string
        print(i)

# End of compareDir method


# Check if original path exists
if os.path.exists(original) and os.path.isdir(original):

    # Check if backup path exists
    if os.path.exists(backup) and os.path.isdir(backup):

        # Make a list of files from both directories
        oList = listDir(original)
        bList = listDir(backup)

        compareDir(oList, bList)