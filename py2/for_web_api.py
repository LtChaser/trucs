import urllib2
import urllib
import sys
import re

#robotList = ['172.29.61.21', '172.29.61.22', '172.29.61.23' ...]
#ip = robotList[robot_number]

if len(sys.argv) > 1:
	robot_number = int(sys.argv[1])
else:
	print "Replay Robot to call (1-26): "
	robot_number = int(raw_input())

robotip = '172.29.61.' + str(robot_number + 10)
uuid = '0'

def getCall(ip):
	ip = str(ip)
	urlGet = str("http://" + ip + "/api/v2/task_instances")
	
	apiInfo = urllib2.urlopen(urlGet).read()
	blockList = re.findall(r'\{(.*?)\}', apiInfo) # create a list of task block
	print blockList
	for block in blockList:
		if 'Replay_Day_0' in block:
			uuidList = re.findall(r'"uuid":"(.*?)","task_name":"Replay_Day_0"', block) # Match uuid between uuid and Replay[_Day_0] => Change "Replay" to match other uuids 
	uuid = uuidList[0]
	return uuid

	
def postCall(ip, uuid):
	urlPost = "http://" + ip + "/api/v2/manager/task_instances/" + uuid
	print "Please enter parameters"
	crid = str(raw_input("crid: "))
	post_data = {'CRID': crid}     # Set POST fields here
	print post_data
	result = urllib2.urlopen(urlPost, urllib.urlencode(post_data))
	content = result.read()
	print content
	
uuid = getCall(robotip)
postCall(robotip, uuid)
	

	
	#{'channelCode': '005', 'epgDay': "2", 'counterBack': 0}
	#	DMA format: paramNAme1:paramValue1,paramNAme2:paramValue2



#http://ip_maestro/api/v1/tasks/task_id/instances/instance_id/runs
#/api/v2/manager/task_instances/12b928c4-e92d-4d5e-a6ef-b637a29ddd6a

#print "http://" + ip + "/api/v2/manager/task_instances/" + uuid