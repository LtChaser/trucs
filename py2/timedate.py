from datetime import datetime
import re 

pgrtime = "09:15-10:15"
strip = re.findall('\d\d:\d\d', pgrtime)

endTime = strip[1]

endTime = datetime.strptime(endTime, '%H:%M').time()
currentTime = datetime.now().time()

if endTime < currentTime:
	print True
	



print endTime
print datetime.now().time()