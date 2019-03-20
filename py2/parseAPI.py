#https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid:~~2F~~2Fbds.tv~~2F275132627-imi:0010000000D5A7B6?byLocationId=24443942973

import urllib2
import json
import re
import time

url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid:~~2F~~2Fbds.tv~~2F275132627-imi:0010000000D5A7B6?byLocationId=24443942973'

data = urllib2.urlopen(url).read()
d = json.loads(data)
	
id1 = d['mediaGroupId']
id2 = d['id']
title = d['program']['title']
title = re.sub(" ", "-", title)

startTime = str(d['actualEndTime'])
startTime = startTime[:-3]
intTime = int(startTime)
pgrDate = time.strftime('%d/%m/%Y', time.localtime(intTime))
	
ret_url = 'https://www.ziggogo.tv/nl/tv/channel-asset.html/' + id1 + '/' + title + '/' + id2 + '/' + title + '.html'

print pgrDate