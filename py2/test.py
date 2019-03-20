import re

loop_iterator = 0

crid = "crid://bds.tv/273719482 imi:0010000000D1D875| crid://bds.tv/721482363 imi:0010000000DA9FE2| crid://bds.tv/721482365 imi:0010000000DA9FE1"
crid = re.sub('\[', '', crid)
crid = re.sub('\]', '', crid)


cridList = crid.split('|')

PGRcrid = cridList[loop_iterator]

print PGRcrid

valueTemp = round(int("120")/(1000))

# #

channelListTemp = [ int(i) for i in ["10"].strip('[]').split(',')]












