import os
import sqlite3
import shutil

safariDatabaseFilename = 'History.db'
safariHistoryDatabasePath = os.path.expanduser('~') + '/Library/Safari/'
safariHistoryDatabaseCopyPath = os.path.join('.', safariDatabaseFilename)

firefoxDatabaseFilename = 'places.sqlite'
firefoxHistoryDatabasePath = os.path.expanduser('~') + '/Library/Application Support/Firefox/Profiles/'
firefoxHistoryDatabasePath += os.listdir(firefoxHistoryDatabasePath)[0]
firefoxHistoryDatabaseCopyPath = os.path.join('.', firefoxDatabaseFilename)

def checkForExistingDataBaseCopies():
    if os.path.isfile(safariHistoryDatabaseCopyPath) != True and os.path.isfile(firefoxHistoryDatabaseCopyPath) != True:
        print('Please copy the following files into this directory first: ' + os.getcwd())
        print(os.path.join(safariHistoryDatabasePath , safariDatabaseFilename))
        print(os.path.join(firefoxHistoryDatabasePath, firefoxDatabaseFilename))
        print('Terminating.')
        quit()

def getSafariHistoryItemsFromDatabase():
    # note: visit_time is stored in number of seconds since January 1, 2001 UTC
    connSafari = sqlite3.connect(safariHistoryDatabaseCopyPath)
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

def getFirefoxHistoryItemsFromDatabase():
    # note: visit_time is a UNIX timestamp
    connFirefox = sqlite3.connect(firefoxHistoryDatabaseCopyPath)
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

def showItemCountOfDataBases():
    print('Found ' + str(len(getSafariHistoryItemsFromDatabase())) + ' Safari history items.')
    print('Found ' + str(len(getFirefoxHistoryItemsFromDatabase())) + ' Firefox history items.')

def copyDataFromSafariToFirefox():
    safariHistoryItems = getSafariHistoryItemsFromDatabase()
    for safariHistoryRow in safariHistoryItems:
        #TODO build the sql insert statement
        #TODO add 978307200 seconds to visit_time to get a UNIX timestamp
        #TODO generate the url_hash
        #TODO generate the guid
        print(safariHistoryRow)
        break

checkForExistingDataBaseCopies()
showItemCountOfDataBases()
copyDataFromSafariToFirefox()

print('Finished. Please clean up the working directory: ' + os.getcwd())
