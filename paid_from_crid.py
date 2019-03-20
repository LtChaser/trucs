import re
import sys
import time
import csv

if len(sys.argv) > 1:
    crid_list = sys.argv
    del crid_list[0]
else:
    paid = raw_input("CRID list (space separated): ")
    crid_list = paid.split(' ')

nowtime = time.strftime("%Y%m%dT%H%M%S")
csv_name = 'C:\\Airflow Report\\failing_crids-{}.csv'.format(nowtime)
cell_title = ['Airflow Crid', 'Human crid', 'Provider', 'Paid'] 
with open(csv_name, 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	writer.writerow(cell_title)

for crid in crid_list:
	print('___________________________________________________________________')
	paid = re.sub(r'uk-crid~~3A~~2F~~2Fog.libertyglobal.com~~2F.*2F', '', crid)
	paid = re.sub(r'-.*', '', paid)
	provider = re.sub(r'uk-crid~~3A~~2F~~2Fog.libertyglobal.com~~2F', '', crid)
	provider = re.sub(r'~~2F.*', '', provider)
	human_crid = re.sub(r'~~3A', ':', crid)
	human_crid = re.sub(r'~~2F', '/', human_crid)
	human_crid = re.sub(r'uk-', '', human_crid)
	human_crid = re.sub(r'-.*', '', human_crid)
	data = [crid, human_crid, provider, paid]
	with open(csv_name, 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
		writer.writerow(data)
    #print('PAID: {}'.format(paid))
    #print('PROVIDER: {}'.format(provider))
    #print('CRID: {}'.format(human_crid))
    #print('___________________________________________________________________')
#uk-crid~~3A~~2F~~2Fog.libertyglobal.com~~2FHIS~~2FPAID0000000001587112-2018-07-31T18:50:14.219692