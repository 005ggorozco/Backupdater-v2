# BACKUPDATER V2 by Gabriel Orozco
# Created on April 4, 2026

# Libraries
import os
import shutil
import time
import progressbar
import colorama

from colorama import Fore, Style
colorama.init(autoreset = True)

original = "Path of the folder to be backed up goes here" 
backup = "Path of backup folder goes here"
interval = 600 # In seconds

# List files of a directory
def listDir(path):
    fileList = []
    
    for root, subroot, files in os.walk(path):
        # Iterate through file list from os.walk()
        for f in files:
            # Remove root from path using slicing (+1 to include slash)
            # Then add to list
            fileList.append(os.path.join(root, f)[ len(path)+1 : ])

    return fileList
# End of listDir()

# Update the backup folder
def backupdate(list1, list2):
    filesToBackup = []

    # Remove files present in 'backup' that are not present in 'original'
    # before comparing both lists

    # Iterate through a copy of list2
    for i in list2[ : ]:
        if i not in list1:
            # Remove by value not by index
            list2.remove(i)

    # Check for files that are missing in backup by
    # iterating through a copy of list1 as well
    for i in list1[ : ]:
        if i not in list2:
            # Add missing files to list
            filesToBackup.append(i)
            # Remove from list1 so that it wont be checked later when comparing files
            list1.remove(i) 

    missingFiles = len(filesToBackup)
    # Set text to Red if there are missing files, otherwise, set to Green
    mNumColor = Fore.RED if missingFiles > 0 else Fore.GREEN

    print(f"{Fore.YELLOW}{Style.BRIGHT}There are{Fore.MAGENTA} ( {mNumColor}{missingFiles}{Fore.MAGENTA} ){Fore.YELLOW} file/s missing from your backup.")

    # Iterate through the remaining files in list1
    for i in list1:
        oPath = os.path.join(original, i)
        bPath = os.path.join(backup, i)

        # Lmt - last modified time
        # Get last modified time of files from original and backup folder
        oLmt = os.path.getmtime(oPath)
        bLmt = os.path.getmtime(bPath)

        if oLmt != bLmt:
            # If their last modified times are not equal, add to list 
            filesToBackup.append(i)

    # Subtract number of missing files to get the number of out-of-date files
    oodFiles = len(filesToBackup) - missingFiles
    # Set text to Red if there are missing files, otherwise, set to Green
    ftbNumColor = Fore.RED if oodFiles > 0 else Fore.GREEN
    print(f"{Fore.YELLOW}{Style.BRIGHT}There are{Fore.MAGENTA} ( {ftbNumColor}{oodFiles}{Fore.MAGENTA} ){Fore.YELLOW} file/s that are out-of-date.\n")

    # Only run this block when there are files to backup
    if len(filesToBackup) > 0:
        print(f"Backing up {len(filesToBackup)} files...")
        # Progress bar stuff
        pBar = progressbar.ProgressBar( max_value = len(filesToBackup) )
        pBar.start()

        for i in range(len(filesToBackup)):
            oPath = os.path.join(original, filesToBackup[i])
            bPath = os.path.join(backup, filesToBackup[i])
            # To get head and tail
            # Head - where the file is located
            # Tail - the file itself
            pathPart = os.path.split(bPath) 

            # In case any Exception occurs during the backup process
            try:    
                if not os.path.exists(pathPart[0]):
                    # Create directory if it doesnt exist
                    os.makedirs(pathPart[0]) 
                    # Then backup
                    shutil.copy2(oPath, bPath) 
                else:
                    shutil.copy2(oPath, bPath) 

            except Exception as e:
                print(e)
                print(f"Unable to backup: {filesToBackup[i]}")

            # Progress bar stuff as well
            pBar.update(i)
        pBar.finish()

        print(f"{Fore.CYAN}{Style.BRIGHT}Done.\n")
# End of backupdate()


while True:
# Check if original path exists
    if os.path.exists(original) and os.path.isdir(original):
        # Check if backup path exists
        if os.path.exists(backup) and os.path.isdir(backup):

            # Make a list of files from both directories
            oList = listDir(original)
            bList = listDir(backup)

            backupdate(oList, bList)
            print(f"{Fore.BLUE}{Style.BRIGHT}Backup is up-to-date.")
            time.sleep(interval) # Run again after set interval
        else:
            print(f"\"{backup}\" does not exist. Please provide a valid backup path.")
            break
    else:
        print(f"\"{original}\" does not exist. Please provide a valid folder path.")
        break