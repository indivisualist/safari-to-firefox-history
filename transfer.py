import os
import sqlite3
import shutil

# DB file names
dbNameSafari = 'History.db'
dbNameFirefox = 'places.sqlite'

# get path to Safari history database
dataPathSafari = os.path.expanduser('~') + '/Library/Safari/'
historySafari = os.path.join(dataPathSafari, dbNameSafari)
# get copied path to Safari history database
dataPathCopySafari = os.path.join('.', dbNameSafari)

# get path to Firefox history database for the first profile
dataPathFirefox = os.path.expanduser('~') + '/Library/Application Support/Firefox/Profiles/'
dataPathFirefox = dataPathFirefox + os.listdir(dataPathFirefox)[0]
historyFirefox = os.path.join(dataPathFirefox, dbNameFirefox)
# get copied path to Firefox history database
dataPathCopyFirefox = os.path.join('.', dbNameFirefox)

# check for previous DB copies and prompt to copy manually. this prevents locking issues
if os.path.isfile(dataPathCopySafari) != True and os.path.isfile(dataPathCopyFirefox) != True:
    print('Please copy the following files into this directory first: ' + os.getcwd())
    print(historySafari)
    print(historyFirefox)
    print('Terminating.')
    quit()

# open history databases
connSafari = sqlite3.connect(dataPathCopySafari)
connFirefox = sqlite3.connect(dataPathCopyFirefox)

# test Safari DB
cSaf = connSafari.cursor()
for row in cSaf.execute('select count(*) from history_items'):
    print(row)
    
# test Firefox DB
cFir = connFirefox.cursor()
for row in cFir.execute('select count(*) from moz_places'):
    print(row)

# clean up
connSafari.close()
connFirefox.close()

# prompt to copy manually and clean up
print('Finished. Please clean up the working directory: ' + os.getcwd())
