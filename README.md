# Backupdater v2

This is a simple Python script to help you automatically back up your files. The script runs _ seconds based on the interval you set. 

## How to setup?
First, open the script on your desired text editor and set the `original` variable to the path of the folder you want to back up and `backup` to your backup folder.

```python
original = "path of the folder you want to back up"
backup = "path of your back up folder"
```

 Make sure to use forwardslashes `/` or double backslashes `\\` and **NOT** single backslashes `/`. 

The file runs and checks for changes in your `original` folder and backs those changes up to your `backup` folder every _ seconds based on an interval you set. By default, the value set is `600` which means your folder is getting backed up every 10 minutes. To change this value, edit the `interval` and give whatever value you want. 

```python
interval = 900 # for 15 minutes
```

**Take note** that the value you set is in **seconds**. 

Once you've set all this up, you can then run this script from anywhere.