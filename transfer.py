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
    connFirefox = sqlite3.connect(firefoxHistoryDatabaseCopyPath)
    cFir = connFirefox.cursor()
    safariHistoryItems = getSafariHistoryItemsFromDatabase()
    for safariHistoryRow in safariHistoryItems:
        # note: visit_time stored in seconds since January 1, 2001 UTC. subtraction gets a UNIX timestamp.
        safariVisitDate = str(float(safariHistoryRow[0]) - float(978307200))
        safariTitle = str(safariHistoryRow[1])
        safariUrl = str(safariHistoryRow[2])
        safariVisitCount = str(safariHistoryRow[3])
        #TODO generate the guid as string
        generatedGuid = "123"
        #TODO generate the url_hash
        generatedUrlHash = "456"

        sql1 = 'insert into moz_places (url, title, visit_count, guid, url_hash) ' \
            'values ("'+safariUrl+'", "'+safariTitle+'", '+safariVisitCount+', "'+generatedGuid+'", "'+generatedUrlHash+'")'
        print(sql1) #debug
        cFir.execute(sql1)

        insertedRowId = str(cFir.lastrowid)
        sql2 = 'insert into moz_historyvisits (place_id, visit_date) ' \
            'values ('+insertedRowId+', '+safariVisitDate+')'
        print(sql2) #debug
        cFir.execute(sql2)

        break #debug
    connFirefox.close()

checkForExistingDataBaseCopies()
showItemCountOfDataBases()
copyDataFromSafariToFirefox()

print('Finished. Please clean up the working directory: ' + os.getcwd())
