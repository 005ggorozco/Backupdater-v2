# Backupdater v2 by Gabriel Orozco
# Created on April 4, 2026

# libraries
import os
import shutil
import progressbar
import time
import colorama

from colorama import Fore, Style
colorama.init(autoreset = True)

# Path of the folder to be backed up
original = "portfolio" 
backup = "bak"
interval = 1000 # in seconds

# List files of a directory method
def listDir(path):
    fileList = []
    
    for root, subroot, files in os.walk(path):
        # Iterate through file list from os.walk()
        for f in files:
            # Remove root from path using slicing (using where root ends) and append to list
            # +1 to remove slash
            fileList.append(os.path.join(root, f)[ len(path)+1 : ])

    return fileList
# End of listDir method

# Update the backup folder
def backupdate(list1, list2):
    filesToBackup = []

    # Remove elements present in backup that are not present in original
    # before comparing both lists

    # Iterate through a copy of list2
    for i in list2[ : ]:
        if i not in list1:
            # Remove by value not by index
            list2.remove(i)

    # Check for files that are missing in backup

    for i in list1[ : ]:
        if i not in list2:
            # add to missing files list
            filesToBackup.append(i)
            list1.remove(i) # remove from list1 so that it wont be checked later when comparing files

    missingFiles = len(filesToBackup)
    mNumColor = Fore.RED if missingFiles > 0 else Fore.GREEN

    print(f"{Fore.YELLOW}{Style.BRIGHT}There are{Fore.MAGENTA} ( {mNumColor}{missingFiles}{Fore.MAGENTA} ){Fore.YELLOW} file/s missing from your backup.")

    # 
    for i in list1:
        # lmt - last modified time
        # get last modified time of files from each path
        oPath = os.path.join(original, i)
        bPath = os.path.join(backup, i)

        oLmt = os.path.getmtime(oPath)
        bLmt = os.path.getmtime(bPath)

        if oLmt != bLmt:
            filesToBackup.append(i)

    ftbNumColor = Fore.RED if (len(filesToBackup) - missingFiles) > 0 else Fore.GREEN
    print(f"{Fore.YELLOW}{Style.BRIGHT}There are{Fore.MAGENTA} ( {ftbNumColor}{ len(filesToBackup) - missingFiles }{Fore.MAGENTA} ){Fore.YELLOW} file/s that are out-of-date.\n")

    # only run this block when there are files to backup
    if len(filesToBackup) > 0:
        print(f"Backing up {len(filesToBackup)} files...")
        pBar = progressbar.ProgressBar( max_value = len(filesToBackup) )
        pBar.start()

        for i in range(len(filesToBackup)):
            oPath = os.path.join(original, filesToBackup[i])
            bPath = os.path.join(backup, filesToBackup[i])
            pathPart = os.path.split(bPath) # to get head and tail

            if not os.path.exists(pathPart[0]):
                os.makedirs(pathPart[0]) # create directory if it doesnt exist
                shutil.copy2(oPath, bPath) # then backup
                #print(i+1)
            else:
                shutil.copy2(oPath, bPath) # then backup'''
            
            pBar.update(i)
        pBar.finish()

        print(f"{Fore.CYAN}{Style.BRIGHT}Done.\n")

# Check if original path exists
#while True:
if os.path.exists(original) and os.path.isdir(original):
    # Check if backup path exists
    if os.path.exists(backup) and os.path.isdir(backup):

        # Make a list of files from both directories
        oList = listDir(original)
        bList = listDir(backup)

        backupdate(oList, bList)
        print(f"{Fore.BLUE}{Style.BRIGHT}Backup is up-to-date.")
        #time.sleep(interval)