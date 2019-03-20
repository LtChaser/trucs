#Poster Presence

import urllib2
import json
import re
import time

# With real POSTER
#url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid%3A~~2F~~2Fbds.tv~~2F718803871-imi%3A0010000000D904C5?byLocationId=24443942973'

# With DEFAULT POSTER
url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid%3A~~2F~~2Fbds.tv~~2F718083682-imi%3A0010000000D8F682?byLocationId=24443942973'

data = urllib2.urlopen(url).read()
d = json.loads(data)

#Get Title of PGR and two IDs needed to build PGR details page URL	
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
	poster = d['program']['images'][0]['url']
	print(poster)
	regex = 'images-nl-dynamic.horizon.tv/EventImages/\d\d\d\d\d\d\d\d\d\d\d.p.jpg'
	if re.match(regex, poster[13:]): 
		posterPresence = 0 # Regex is associated with default POSTER type of URLs as opposed to PGR specific poster which possess different link shape
	else:
		posterPresence = 1 # Therefore if links does not match. We conclude the presence of PGR specific poster
	
except:
	posterPresence = 0  # It can happen that no link at all is present in the API (JSON data cannot be parsed). On the PGR page no poster will show neither default nor PGR specific poster.
	
ret_url = 'https://www.ziggogo.tv/nl/tv/channel-asset.html/' + id1 + '/' + title + '/' + id2 + '/' + title + '.html'

print posterPresence
print '##################################'
print pgrDate

#Default POSTER Regex

#print poster[13:]
print 'regex is equal to url: '


