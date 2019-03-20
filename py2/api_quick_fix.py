import urllib2
import urllib
import sys
import re

urlPost = "http://172.29.63.249/api/v2/manager/task_instances/dfb4dfac-d5a5-4072-9d72-8ec9faab12c4"
post_data = {}
result = urllib2.urlopen(urlPost, urllib.urlencode(post_data))
print result