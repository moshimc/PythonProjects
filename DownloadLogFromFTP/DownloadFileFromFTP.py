#! python3
#Inventory Log Download


# ----------------------------------------
# Imports
# ----------------------------------------
from ftplib import FTP


# ----------------------------------------
# Properties
# ----------------------------------------
path = '/logs/'
filename = 'inventory.txt'


# ----------------------------------------
# Name: downloadLogFile
# Abstract: downloads txt file from FTP
# ----------------------------------------
def downloadLogFile(pathToFile, fileName):
    ftp = FTP('10.1.100.126')
    ftp.login(user='<username>', passwd = '<password>')
    print('Successfully Logged In')
    ftp.cwd(pathToFile)
    localfile = open('C:\\Users\\TD Programmer\\reports\\' + fileName, 'wb')
    print('Downloading ' + fileName)
    ftp.retrbinary("RETR " + fileName, localfile.write)
    ftp.quit()
    localfile.close()
    print('File written')


# ----------------------------------------
# START
# ----------------------------------------
downloadLogFile(path, filename)
