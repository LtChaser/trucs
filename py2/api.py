import urllib2
import urllib
import sys
import re

#robotList = ['172.29.61.21', '172.29.61.22', '172.29.61.23']
#ip = robotList[robot_number]

if len(sys.argv) > 1:
	robot_number = int(sys.argv[1])
else:
	print("Robot to call (1-*): ")

robot_number = raw_input()
task_name = raw_input("Task name: ")

		
		
if robot_number == 'lab' or robot_number == 'LAB':
	robotip = '172.29.63.147'
elif robot_number == 'choose ip' or robot_number == str(0):
	robotip = raw_input('Robot IP: ')
else:
	robotip = '172.29.61.' + str(int(robot_number) + 10)
	uuid = '0'

def getCall(ip):
	ip = str(ip)
	urlGet = str("http://" + ip + "/api/v2/task_instances")
	
	apiInfo = urllib2.urlopen(urlGet).read()
	blockList = re.findall(r'\{(.*?)\}', apiInfo) # create a list of task block
	for block in blockList:
		if 'Replay' in block or "Startover" in block or 'Robustness Test' in block:
			uuidList = re.findall(r'"uuid":"(.*?)","task_name":'.format(task_name), block)
			#uuidList = re.findall(r'"uuid":"(.*?)","task_name":"Replay', block) # Match uuid between uuid and Replay[_Day_0] => Change "Replay" to match other uuids 
	uuid = uuidList[0]
	return uuid

	
def postCall(ip, uuid, task_name):
	urlPost = "http://" + ip + "/api/v2/manager/task_instances/" + uuid
	if task_name == 'Replay' or task_name == 'Startover':
		print("Please enter parameters")
		chanCode = str(raw_input("channelCode: " ))
		eDay = str(raw_input("epgDay: " ))
		countBack = str(raw_input("counterBack: "))
		crid = str(raw_input("crid: "))
		post_data = {'channelCode': chanCode, 'epgDay': eDay, 'counterBack': countBack, 'crid': crid}     # Set POST fields here
		print(post_data)
	else:
		post_data = {}
	result = urllib2.urlopen(urlPost, urllib.urlencode(post_data))
	content = result.read()
	print(content)
	
uuid = getCall(robotip)
postCall(robotip, uuid, task_name)
	

	
	#{'channelCode': '005', 'epgDay': "2", 'counterBack': 0}
	#	DMA format: paramNAme1:paramValue1,paramNAme2:paramValue2



#http://ip_maestro/api/v1/tasks/task_id/instances/instance_id/runs
#/api/v2/manager/task_instances/12b928c4-e92d-4d5e-a6ef-b637a29ddd6a

#print "http://" + ip + "/api/v2/manager/task_instances/" + uuid