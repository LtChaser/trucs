import datetime
import time


now = datetime.datetime.now()
print('Week nb {}'.format(now.isocalendar()[1]))
time.sleep(5)
