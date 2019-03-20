import re

crid = '[crid://bds.tv/273979242 imi:0010000000D2E52F|crid://bds.tv/273979242 imi:0010000000D2E52F|crid://bds.tv/273979242 imi:0010000000D2E52F]'
crid = re.sub('\[', '', crid)
crid = re.sub('\]', '', crid)
crid = re.sub(' ', '-', crid)


cridList = crid.split('|')

print cridList



