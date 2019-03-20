import urllib2
import urllib
import sys
import re

# robotList = ['172.29.61.21', '172.29.61.22', '172.29.61.23' ...]
# ip = robotList[robot_number]

if len(sys.argv) > 1:
    robot_number = int(sys.argv[1])
else:
    print("Robot to call (1-*): ")

robot_number = raw_input()
task_name = 'HZN_Maintenance_Campaign_2'

if robot_number == 'lab' or robot_number == 'LAB':
    robotip = '172.29.63.147'
else:
    robotip = '172.29.61.' + str(int(robot_number) + 10)
    uuid = '0'


def getCall(ip):
    ip = str(ip)
    urlGet = str("http://" + ip + "/api/v2/task_instances")

    apiInfo = urllib2.urlopen(urlGet).read()
    blockList = re.findall(r'\{(.*?)\}', apiInfo)  # create a list of task block
    for block in blockList:
        if 'HZN_Maintenance_Campaign_2' in block:
            uuidList = re.findall(r'"uuid":"(.*?)","task_name":'.format(task_name), block)
        # uuidList = re.findall(r'"uuid":"(.*?)","task_name":"Replay', block) # Match uuid between uuid and Replay[_Day_0] => Change "Replay" to match other uuids
    uuid = uuidList[0]
    return uuid


def postCall(ip, uuid):
    urlPost = "http://" + ip + "/api/v2/manager/task_instances/" + uuid
    result = urllib2.urlopen(urlPost, urllib.urlencode())
    content = result.read()
    print(content)


uuid = getCall(robotip)
postCall(robotip, uuid)

# {'channelCode': '005', 'epgDay': "2", 'counterBack': 0}
#	DMA format: paramNAme1:paramValue1,paramNAme2:paramValue2


# http://ip_maestro/api/v1/tasks/task_id/instances/instance_id/runs
# /api/v2/manager/task_instances/12b928c4-e92d-4d5e-a6ef-b637a29ddd6a

# print "http://" + ip + "/api/v2/manager/task_instances/" + uuid