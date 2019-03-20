#!/usr/bin/python
import urllib2
import urllib


url_list = [
    'https://repo.saltstack.com/',
    'https://download.postgresql.org',
    "https://witbe.bintray.com",
    'https://github.com',
    'https://idmsa.apple.com',
    'https://developerservices2.apple.com',
    'https://developer.apple.com',
    'https://itunesconnect.apple.com',
    'https://du-itc.itunesconnect.apple.com',
    'https://chocolatey.org/',
    'https://api.bintray.com/',
	'https://www.witbe.net'
    ]

# encoded_url = urllib2.encode(url)



username = '87ed0cd35803039f@witbe'
password = '4080a74b5f3576328ff95d36be2d9b647e428940'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()


failure_list = []

for url in url_list:
    p.add_password(None, url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    try:
        resp = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print('{} has thrown {}'.format(url, e))
        failure_list.append(url)
    except urllib2.URLError as e:
        print('{} could not be resolved. Exception: {}'.format(url, e))
        failure_list.append(url)
    else:
        resp_code = resp.getcode()
        if resp_code == 200:
            print('{} is reachable'.format(url))
        else:
            print('{} is unreachble with response code: {}'.format(url, resp_code))


if failure_list == ['https://idmsa.apple.com', 'https://developerservices2.apple.com', 'https://du-itc.itunesconnect.apple.com', 'https://api.bintray.com/']:
    print('Expected URLs threw an error. Consider success.')
else:
    print('Following URLs have thrown an error: ')
    for i in failure_list:
        print(i)