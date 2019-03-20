import urllib2
import urllib
import sys

ip = sys.argv[1]
uuid = sys.argv[2]

url = "http://" + ip + "/api/v2/manager/task_instances/" + uuid
post_data = {'channelCode': '007', 'epgDay': '6'}     # Set POST fields here

result = urllib2.urlopen(url, urllib.urlencode(post_data))
content = result.read()
print content


#http://ip_maestro/api/v1/tasks/task_id/instances/instance_id/runs
#/api/v2/manager/task_instances/12b928c4-e92d-4d5e-a6ef-b637a29ddd6a

print "http://" + ip + "/api/v2/manager/task_instances/" + uuid