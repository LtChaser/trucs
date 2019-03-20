from urllib import request
from datetime import datetime, timedelta, time
import pdb
# import datetime
import os
import re

#

# NPO3 13:01 insterted (13:00 run)
# Video = 2017 11 28 12 01 01
# http://172.29.61.13/static/data/traces/video/2017/11/28/20171128120101.mkv
# good:  20171128 16 07 10       BAD:    20171128 16 12 23

# timestamp = input("timestamp: ")

def download(file_name, dirs_name):
  filename = dirs_name.replace("/", "") + file_name + ".mkv"
  dt_object = datetime.strptime(dirs_name, '%Y/%m/%d')
  print(dt_object)
  dir = dt_object.strftime('%Y/%#m/%#d')
  print(dir)
  
  url = "http://172.29.61.15/static/data/traces/video/" + dir + "/" + filename
  print(url)
  vid = request.urlopen(url).read()
  print(vid)
  path = "C:\Traces"
  os.chdir(path)
  with open(filename, 'wb') as f:
    f.write(vid)
	
def filename():
	pass # Built from
	date_format = re.findall('\d\d\d\d-\d\d-\d\d', date) #date is from input
	date_to_pass = date_format[0].replace("-", "/")
	filename = date_to_pass.replace("/", "") + file_name + ".mkv"
	
def build_url():
	vid_datetime = vid_datetime + timedelta(seconds=1)
	vid_time = str(vid_datetime.time())
	filename = vid_time.replace(":", "")
    filename = dirs_name.replace("/", "") + filename + ".mkv"

# PlaceHolder
# date = "2017-11-28 13:01:27"
# 2018-02-09 09:40:41

date = input("Timestamp: ")

## Directories
date_format = re.findall('\d\d\d\d-\d\d-\d\d', date)

print("Passing date: " + date_to_pass)

## Filename
date_for_file = re.findall('\d\d\d\d-\d\d-\d\d \d\d:\d\d', date)
date_for_file = date_for_file[0] + ':00'
date_object = datetime.strptime(date_for_file, '%Y-%m-%d %H:%M:%S')
vid_datetime = date_object - timedelta(hours=1, seconds=361)  # seconds - 1 to start loop at HH:MM:00


#pdb.set_trace()
for i in range(0, 361):
  filename = filename()
  url = build_url(filename)
  vid_datetime = vid_datetime + timedelta(seconds=1)
  vid_time = str(vid_datetime.time())
  vidtime_format = vid_time.replace(":", "")
  #print(vidtime_format)
  try:
   download(vidtime_format, date_to_pass)
  except:
   pass


#def tmp():
#    time = re.findall('\d\d:\d\d:\d\d', time)
#    time1 = datetime.datetime.strptime(time[0], '%H:%M:%S').time()
#    print(time)
#    print(type(time1))
#    tmp_datetime = datetime.datetime.combine(datetime.date.today(), time1)
#    vidtime = (tmp_datetime - timedelta(hours=1))
#    print(vidtime)
