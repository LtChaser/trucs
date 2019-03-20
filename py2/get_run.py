import urllib2


ip = "172.29.61.36"
urlGet = str("http://" + ip + "/api/v2/manager/runs")

print urlGet
	
apiInfo = urllib2.urlopen(urlGet).read()

print apiInfo