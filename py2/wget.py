import sys
import ftplib
import os
from ftplib import FTP

ftp=FTP('home322951469.1and1-data.host')
ftp.login('u58223677','Adrenaline31')
def downloadFiles(source,destination):
#source & destination are str of the form "/dir/folder/something/"
#source should be the abs source to the root FOLDER of the file tree to download
    try:
        ftp.cwd(source)
        #clone source to destination
        os.chdir(destination)
        os.mkdir(destination[0:len(destination)-1]+source)
        print destination[0:len(destination)-1]+source+" built"
    except OSError:
        #folder already exists at destination
        pass
    except ftplib.error_perm:
        #invalid entry (ensure input form: "/dir/folder/something/")
        print "error: could not change to "+source
        sys.exit("ending session")

    #list children:
    filelist=ftp.nlst()

    for file in filelist:
        try:
            #this will check if file is folder:
            ftp.cwd(source+file+"/")
            #if so, explore it:
            downloadFiles(source+file+"/",destination)
        except ftplib.error_perm:
            #not a folder with accessible content
            #download & return
            os.chdir(destination[0:len(destination)-1]+source)
            #possibly need a permission exception catch:
            ftp.retrbinary("RETR "+file, open(os.source.join(destination,file),"wb").write)
            print file + " downloaded"
    return

source= 'TestDir/'
dest= 'C:\\TestBackup'
downloadFiles(source,dest)

