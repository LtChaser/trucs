import re

# Format Received =  crid://bds.tv/50745636 imi:0010000000D56A4C
# WithPoster      =  crid://bds.tv/714111494 imi:0010000000D56627
# Without Poster  =  crid://bds.tv/716432295 imi:0010000000D6D6F5
					 crid://bds.tv/248460897 imi:0010000000D57A5E


# Web Format =   crid%3A~~2F~~2Fbds.tv~~2F275234496-imi%3A0010000000D63CF9
# Result     =   crid%3A~~2F~~2Fbds.tv~~2F275234496-imi%3A0010000000D63CF9
#			 =   crid%3A~~2F~~2Fbds.tv~~2F275234496-imi%3A0010000000D63CF9


# crid://bds.tv/275234496 imi:0010000000D63CF9

crid = 'crid://bds.tv/275234496 imi:0010000000D63CF9'


if crid.startswith('CRID:crid'):
	crid = re.sub('CRID:', '', crid)

try:
	webcrid = re.sub(':', '%3A', crid)
	webcrid = re.sub('/', '~~2F', webcrid)
	finalcrid = re.sub(' ', '-', webcrid)
	url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/' + finalcrid

	
	
except:
	pass
	
print url