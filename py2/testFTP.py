import sys
import ftplib
import os
from ftplib import FTP
ftp=FTP("home322951469.1and1-data.host")
ftp.login("u58223677","Adrenaline31")

def downloadFiles(path,destination):
	try:
		ftp.cwd(path)
		os.chdir(destination)
		os.mkdir(destination+path)
		print destination + path
	except OSError:
		pass
	except ftplib.error_perm:
		print "error: could not change to "+path
		sys.exit("ending session")

    #list children:
	filelist=ftp.nlst()

	for file in filelist:    #at 2. we're in /TestDir/subfolder/
		print "destination + path = " + destination + path
		if file != '.' and file != '..':
			try:
			#this will check if file is folder:
				ftp.cwd(path + "/" + file+"/")		#at 2. try /TestDir/subfolder/sububfolder/
            #if so, explore it:
				downloadFiles(path+ "/" + file,destination) #if path is dir recall function   # at 2. we reach end of tree so we dont go there
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