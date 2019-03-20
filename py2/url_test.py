import urllib2
import json
import re

def getData(url):
	
	data = urllib2.urlopen(url).read()
	d = json.loads(data)
	
	id1 = d['mediaGroupId']
	id2 = d['id']
	title = d['program']['title']
	title = re.sub(" ", "-", title)
	
	url = 'https://www.ziggogo.tv/nl/tv/channel-asset.html/' + id1 + '/' + title + '/' + id2 + '/' + title + '.html'
	
	#https://www.ziggogo.tv/nl/tv/channel-asset.html/crid%3A~~2F~~2Fbds.tv~~2F48696657/serious-request-tv/crid%3A~~2F~~2Fbds.tv~~2F711848636-imi%3A0010000000D2A1BD/serious-request-tv.html
	
	
	print url
	print url
	
	
	
getData('https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid:~~2F~~2Fbds.tv~~2F711848636-imi:0010000000D2A1BD?byLocationId=24443942973')