# Safari to Firefox import
Transfer browser history from Safari to Firefox.

With the built-in Firefox Import Wizard, it is currently not possible to import the browser history from Safari to Firefox on macOS. This standalone Python script copies all history entries.

**TODO:** The database seems to be locked and/or messed up when writing, something's not working yet. There are also values which have to be calculated.

## Caveats
*IMPORTANT:* This script is currently work-in-progress and might not behave as expected. Use at your own risk.

* For now, the history files of both browsers have to be copied manually and no backup is created by the script.
* Selection between multiple Firefox profiles is currently not possible, the script automatically selects one. You can adjust the script by hand to choose a specific one.

## Requirements
* access to the history files, e.g. with the macOS Finder or macOS Terminal
* built with Python 3.7, should work with 2.7 as well

## Running
1. clone the repository into a directory you have write access to
1. run `python3.7 transfer.py`
1. follow the directions to copy the history files
1. if necessary, run the script again
1. the script attempts to copy all history entries from Safari to Firefox
1. copy the files back and clean up

Tested with Safari 12.0 and Firefox 64.0 on macOS 10.14 Mojave.