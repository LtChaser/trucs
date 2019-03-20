from ipwhois.experimental import get_bulk_asn_whois
from pprint import pprint


ip_list = ['115.70.29.153',
			'172.217.17.142',
			'65.52.139.168',
			'52.114.32.7',
			'86.160.212.47',
			'83.28.65.1',
			'5.196.71.125',
			'185.21.217.81',
			'239.255.255.250',
			'93.184.220.29']
			
ip = ['40.79.65.235']
					
results = get_bulk_asn_whois(addresses=ip_list)
pprint(results.split('\n'))
