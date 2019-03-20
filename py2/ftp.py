from ftplib import FTP
import os, sys, os.path
import ftplib


def dlBackup(localDir,ftpDir):
	try:
		ftp.cwd(ftpDir)
		os.chdir(local)
		#os.mkdir(local + source)
		print local + source

	except OSError:
        #folder already exists at local
			pass
	except ftplib.error_perm:
			#invalid entry (ensure input form: "/dir/folder/something/")
			print "error: could not change to "+ftpdir
			sys.exit("ending session")
			
	filelist = ftp.nlst()
	for f in filelist:
		if f != '.' and f != '..':
			try: 
				ftp.cwd(ftpDir + f)
				newPath = ftpDir + f + '/'
				dlBackup(newPath, )
			
			except ftp.lib.error.perm:
				local_path = os.path.join(localDir, f)   #maybe user os.path.join to create dirs....
				print local_path
				file = open(local_path, 'wb')
				ftp.retrbinary('RETR ' + f, file.write)
				file.close()
				
		
			
			
serv = 'home322951469.1and1-data.host'
print "Connection...", serv
ftp = FTP(serv)
ftp.login('u58223677','Adrenaline31')
print "Connection etablie"





ftpdir = 'TestDir/'
localDir = 'C:\\TestBackup'

dlBackup(localDir,ftpdir)			
			
			
			
			
			
			
			
			
			
		
ftp.quit()
print "connection closed"