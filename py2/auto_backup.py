from ftplib import FTP
import os, sys, os.path
import ftplib


ftpdir = '\\TestDir'

serv = 'home322951469.1and1-data.host'
print "Connection...", serv
ftp = FTP(serv)
ftp.login('u58223677','Adrenaline31')
print "Connection etablie"



def main():
	
	
	serv = 'home322951469.1and1-data.host'
	print "Connection...", serv
	ftp = FTP(serv)
	ftp.login('u58223677','Adrenaline31')
	print "Connection etablie"
	
	ftpDir = 'TestDir/'
	localDir = 'c:\\TestBackup'

	dir = "C:\\Users\\cou-w\\Documents\\cinemodeles\\testDirr"
	
	print localDir

	ftpBackup(ftpDir, localDir)
	
def ftpBackup(source, local):

	print local

	try:

		ftp.cwd(source)
        #clone source to local
        os.chdir(local)
        os.mkdir(local[0:len(local)-1]+source)
		print local[0:len(local)-1]+source+" built"
		
    except OSError:
        #folder already exists at local
        pass
    except ftplib.error_perm:
        #invalid entry (ensure input form: "/dir/folder/something/")
        print "error: could not change to "+source
        sys.exit("ending session")
	
	filelist = ftp.nlst()
	for f in filelist:
		
		try:
			
			ftp.cwd(ftpDir + f + '/')
			ftpBackup(ftpDir + f + '/', )
			ftp.retrbinary('RETR' + f, file.write)
			
		except ftplib.error_perm:
	
			if f != '.' and f != '..':
			
					print f
					local_path = os.path.join(localDir, f)   #maybe user os.path.join to create dirs....
					print local_path
					file = open(local_path, 'wb')
					ftp.retrbinary('RETR ' + f, file.write)
					file.close()


	ftp.quit()
	print "Connection FTP terminee"
	

	
	
if __name__ == "__main__":
	main()

dir = "C:\\Users\\cou-w\\Documents\\cinemodeles\\testDirr"
os.chdir(dir)
ftp = FTP('home322951469.1and1-data.host')

ftp.login('u58223677','Adrenaline31')


