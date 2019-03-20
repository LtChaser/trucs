#Poster Presence

import urllib2
import json
import re
import time

# With real POSTER
url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid%3A~~2F~~2Fbds.tv~~2F718803871-imi%3A0010000000D904C5?byLocationId=24443942973'

# With DEFAULT POSTER
url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid%3A~~2F~~2Fbds.tv~~2F718083682-imi%3A0010000000D8F682?byLocationId=24443942973'

data = urllib2.urlopen(url).read()
d = json.loads(data)
	
id1 = d['mediaGroupId']
id2 = d['id']
title = d['program']['title']
title = re.sub(" ", "-", title)

# Date
startTime = str(d['endTime'])
startTime = startTime[:-3]
intTime = int(startTime)
pgrDate = time.strftime('%d/%m/%Y', time.localtime(intTime))

#Poster

try:
	poster = d['program']['images']
	listLength = len(poster)
	if listLength > 0:
		posterPresence = 1
	else:
		posterPresence = 0
except:
	posterPresence = 0 
	
ret_url = 'https://www.ziggogo.tv/nl/tv/channel-asset.html/' + id1 + '/' + title + '/' + id2 + '/' + title + '.html'

print posterPresence
print '##################################'
print pgrDate