import os
import sqlite3
import shutil

# DB file names
dbNameSafari = 'History.db'
dbNameFirefox = 'places.sqlite'

# get path to Safari history database
dataPathSafari = os.path.expanduser('~') + '/Library/Safari/'
# get copied path to Safari history database
dataPathCopySafari = os.path.join('.', dbNameSafari)

# get path to Firefox history database for the first profile
dataPathFirefox = os.path.expanduser('~') + '/Library/Application Support/Firefox/Profiles/'
dataPathFirefox = dataPathFirefox + os.listdir(dataPathFirefox)[0]
# get copied path to Firefox history database
dataPathCopyFirefox = os.path.join('.', dbNameFirefox)

# check for previous DB copies and prompt to copy manually. this prevents locking issues
historyFilePathSafari = os.path.join(dataPathSafari, dbNameSafari)
historyFilePathFirefox = os.path.join(dataPathFirefox, dbNameFirefox)
if os.path.isfile(dataPathCopySafari) != True and os.path.isfile(dataPathCopyFirefox) != True:
    print('Please copy the following files into this directory first: ' + os.getcwd())
    print(historyFilePathSafari)
    print(historyFilePathFirefox)
    print('Terminating.')
    quit()

# load Safari DB items
# visit_time is stored in number of seconds since January 1, 2001 UTC
def getSafariHistoryItems():
    connSafari = sqlite3.connect(dataPathCopySafari)
    cSaf = connSafari.cursor()
    cSaf.execute(
        'select visit_time, title, url, visit_count '
        'from history_visits '
        'inner join history_items '
        'on history_visits.history_item = history_items.id '
        )
    rows = cSaf.fetchall()
    connSafari.close()
    return rows

# load Firefox DB items
# visit_time is a UNIX timestamp, so the number of microseconds since January 1, 1970 UTC
def getFirefoxHistoryItems():
    connFirefox = sqlite3.connect(dataPathCopyFirefox)
    cFir = connFirefox.cursor()
    cFir.execute(
        'select visit_date, title, url, visit_count '
        'from moz_historyvisits '
        'inner join moz_places '
        'on moz_historyvisits.place_id = moz_places.id '
        )
    rows = cFir.fetchall()
    connFirefox.close()
    return rows

safariHistoryItems = getSafariHistoryItems()
print('Found ' + str(len(safariHistoryItems)) + ' Safari history items.')
for row in safariHistoryItems:
    print(row)
    break

firefoxHistoryItems = getFirefoxHistoryItems()
print('Found ' + str(len(firefoxHistoryItems)) + ' Firefox history items.')
for row in firefoxHistoryItems:
    print(row)
    break

# prompt to copy manually and clean up
print('Finished. Please clean up the working directory: ' + os.getcwd())
