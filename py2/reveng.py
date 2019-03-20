import sys
import ftplib
import os
from ftplib import FTP
ftp=FTP("home322951469.1and1-data.host")
ftp.login("u58223677","Adrenaline31")

def downloadFiles(path,destination):
#path & destination are str of the form "/dir/folder/something/"
#path should be the abs path to the root FOLDER of the file tree to download
    try:
        ftp.cwd(path)# 1. TRY CDing on /TestDir    2. TRY CDing on /TestDir+file+"/"  (path)
        #clone path to destination
		os.chdir(destination)# 1. TRY CDing on C:\TestBackup (local)  2. TRY CDing on C:\TestBackup (again)
		os.mkdir(destination+path)#os.mkdir(destination[0:len(destination)-1]+path)	 Make directory at   2. Make directory C:\TestBackup/TestDir+file+"/"
        print destination + path + " built"
    except OSError:
        #folder already exists at destination
        pass
    except ftplib.error_perm:
        #invalid entry (ensure input form: "/dir/folder/something/")
        print "error: could not change to "+path
        sys.exit("ending session")

    #list children:
    filelist=ftp.nlst()

    for file in filelist:    #at 2. we're in /TestDir/subfolder/
		
        try:
            #this will check if file is folder:
            ftp.cwd(path+file+"/")		#at 2. try /TestDir/subfolder/sububfolder/
            #if so, explore it:
            downloadFiles(path+file+"/",destination) #if path is dir recall function   # at 2. we reach end of tree so we dont go there
        except ftplib.error_perm:
            #not a folder with accessible content
            #download & return
            os.chdir(destination+path)  # change local dir to "C:\TestBackup"/TestDir+NEWDIR (CREATED IN SECOND CALL OF FUNTION)
            #possibly need a permission exception catch:
            ftp.retrbinary("RETR "+file, open(os.path.join(destination,file),"wb").write)  #DOWNLOAD FILE
            print file + " downloaded"
    return

source="/TestDir"
dest="C:\TestBackup"
downloadFiles(source,dest)