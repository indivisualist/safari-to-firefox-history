# Safari to Firefox import
Transfer browser history from Safari to Firefox.

With the built-in Firefox Import Wizard, it is currently not possible to import the browser history from Safari to Firefox on macOS. This standalone Python script copies all history entries.

## Features
*IMPORTANT:* This script is currently work-in-progress and might not behave as expected. Use at your own risk.

* TODO: automatically copy and back up the history files; for now manual process
* TODO: select between multiple Firefox profiles; for now automatically selects one
* TODO: copy all history entries; for now just prints outs the count to verify the functionality

## Requirements
* access to the history files, e.g. with the macOS Finder or macOS Terminal
* tested with Python 2.7 and 3.7

## Running
1. clone the repository into a directory you have write access to
1. run `python2.7 transfer.py` respectively `python3.7`
1. follow the directions to copy the history files
1. if necessary, run the script again

The script attempts to copy all history entries from Safari to Firefox.

Tested with Safari 12.0 and Firefox 64.0 on macOS 10.14 Mojave.