# Backupdater-v2

This is a second version of a Python script [previously created](https://github.com/Yuure1/Backupdater) to help you automatically back up your files. This script constantly runs with an interval of your own choosing.

## How to setup?
First, open the script on your desired text editor and set the `original` variable to the path of the folder you want to back up and `backup` to your backup folder.

```python
original = "path of the folder you want to back up"
backup = "path of your back up folder"
```

 Make sure to use forwardslashes `/` or double backslashes `\\` and **NOT** single backslashes `\`. 

The file runs and checks for changes in your `original` folder and backs those changes up to your `backup` folder every *n* seconds based on an interval you set. By default, the value is set to `600` and this value is in seconds which means your folder will get backed up every **10 minutes**. To change this value, set the `interval` variable to the value of your liking but take note that it must be a non-negative whole number.

```python
interval = 900 # for 15 minutes
```

Once this is all set up, the script can now be used. It is recommended to set your machine so that it runs this script everytime on boot-up to properly utilize this script.