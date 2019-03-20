import urllib2
import json

def getData(url):
	
	data = urllib2.urlopen(url).read()
	d = json.loads(data)
	
	id1 = d['stationId']
	id2 = int(id1) - 10
	
	ret_url = 'https://www.ziggogo.tv/nl/tv/channel-asset.html/' + id1 + '/location/' + str(id2) + '.html#action=watch'
	
	#https://www.ziggogo.tv/nl/tv/channel-asset.html/24443942983/location/24443942973.html#action=watch
	# https://www.ziggogo.tv/nl/tv/channel-asset.html/crid%3A~~2F~~2Fbds.tv~~2F48696657/serious-request-tv/crid%3A~~2F~~2Fbds.tv~~2F711848636-imi%3A0010000000D2A1BD/serious-request-tv.html
	#Assets Gathering
	#startTime = d['startTime']
	#endTime = d['endTime']
	#title = d['program']['title']
	#posterURL = 'https://wp9-images-nl-dynamic.horizon.tv/EventImages/272855501.p.7eb028d131178881a8f4e3c0db58c0e97c9f215a.jpg?w=180&h=260&mode=box'
	
	print ret_url
	
	
	
	
getData('https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/crid:~~2F~~2Fbds.tv~~2F274792214-imi:0010000000D2A1C8')