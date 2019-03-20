
# To use the input params, simply use d["channelNumber"] d["replayIcon"] d["posterAvailable"] d["pgrName"] d["pgrDate"] d["videoLoadingTime"] d["videoLaunch"] d["trickmodePause"] d["trickmodeForward"] d["trickmodeRewind"] 
# Your code here

##### Input Parameters for Splitted Audio/Video:   audioAvail   /   videoAvail


import socket
import sys
from urllib2 import Request, urlopen
import urllib
import json
import time
import pdb




scriptName = "Replay_Day_0"
robotip = "172.29.61.35"


	
# to send
MEASURE_RUN_ID = "1111"
SCRIPT_NAME = scriptName
ROBOT_IP = robotip
CHANNEL_NUMBER = "1"
REPLAY_ICON_PRESENCE = "1"
POSTER_AVAIL = "1"
PROGRAM_TITLE = "Tis but a test@"
TIMESLOT = "14:00-14:30"
VIDEO_LOADING_TIME = "130"
LAUNCH_VIDEO = "1"
TRICKMODE_PAUSE = "1"
TRICKMODE_FORWARD = "1"
TRICKMODE_REWIND = "1"
AUDIO_AVAIL = "1"
VIDEO_AVAIL = "1"
ASSET_ID = "N/A"
PROGRAM_DAY = "27/02/2018"
PGR_ELAPSED_TIME = "130"


# to build packet
values = { 'MEASURE_RUN_ID': MEASURE_RUN_ID,'SCRIPT_NAME': SCRIPT_NAME,'ROBOT_IP': ROBOT_IP,'CHANNEL_NUMBER': CHANNEL_NUMBER,'REPLAY_ICON_PRESENCE_': REPLAY_ICON_PRESENCE,'POSTER_AVAIL_': POSTER_AVAIL,'PROGRAM_TITLE_': PROGRAM_TITLE,'TIMESLOT_': TIMESLOT,'VIDEO_LOADING_TIME_': VIDEO_LOADING_TIME,'LAUNCH_VIDEO_': LAUNCH_VIDEO,'VIDEO_AVAIL_': VIDEO_AVAIL, 'AUDIO_AVAIL_': AUDIO_AVAIL, 'TRICKMODE_PAUSE_': TRICKMODE_PAUSE,'TRICKMODE_FORWARD_': TRICKMODE_FORWARD,'TRICKMODE_REWIND_': TRICKMODE_REWIND,'ASSET_ID_': ASSET_ID,'PROGRAM_DAY_': PROGRAM_DAY,'PGR_ELAPSED_TIME_': PGR_ELAPSED_TIME }
data = json.dumps(values)

pdb.set_trace()
pathFile = 'C:\\Traces\\'
with open(pathFile+'postdataAsset_0.json', 'w') as outfile:
    json.dump(data, outfile)

request = Request('http://172.29.63.38:8013/post',data, {'Content-Type': 'application/json'})
#request_staging = Request('http://172.29.63.54:8013/post',data, {'Content-Type': 'application/json'})

print request