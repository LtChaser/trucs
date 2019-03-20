import datetime

timeslot1 = '13:00'
timeslot2 = '12:55'

timeObj1 = datetime.datetime.strptime(timeslot1, '%H:%M').time()
timeObj2 = datetime.datetime.strptime(timeslot2, '%H:%M').time()

print 't1: ' , timeObj1
print 't2: ' , timeObj2

if timeObj1 > timeObj2: # TimeObj1 is the value before rewind
	print 'bloup'
else:
	print 'bla'