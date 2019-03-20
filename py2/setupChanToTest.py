import time

channelListTemp = [ int(i) for i in "007".strip('[]').split(',')]
#logging.debug("channelListTemp: %s", channelListTemp)

if channelListTemp:
    myChannelDigit = channelListTemp[int(time.time()/(3600)%len(channelListTemp))]
    channel = list(map(str,str(channelListTemp[int(time.time()/(3600)%len(channelListTemp))])))
	

	
print channelListTemp	
	
print channel
print myChannelDigit