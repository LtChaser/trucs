import csv
import re
import time

paid_to_feed = []
airflow_dump = 'C:\\Airflow Report\\export-20181107.csv'
title_row = ['RunDate', 'CRID/RUN ID', 'Provider', 'PAID', 'LicenceExpiration', 'Details', 'Errors']
nowtime = time.strftime("%Y%m%dT%H%M%S")
report_name = 'C:\\Airflow Report\\ingest_report-{}.csv'.format(nowtime)

with open(report_name, 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(title_row)


def one_way_to_do_it(airflow_dump):

    exec_date = []
    run_ids = []
    paids = []
    providers = []

    with open(airflow_dump) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_nb = 0
        for row in csv_reader:
            if line_nb == 0:
                line_nb += 1
            else:
                crid_cut = re.sub(r'uk-crid~~3A~~2F~~2Fog.libertyglobal.com~~2F', '', row[1])
                providers.append(re.sub(r'~~2F.*', '', crid_cut))
                crid_cut = re.sub('.*~~2F', '', crid_cut)
                paids.append(re.sub(r'-.*', '', crid_cut))
                exec_date.append(re.sub(r' ', 'T', row[4]))
                run_ids.append(row[1])
                line_nb += 1

with open(airflow_dump) as airflow_csv:
    csv_reader = csv.reader(airflow_csv, delimiter=',')
    line_nb = 0
    for row in csv_reader:
        if line_nb == 0:
            line_nb += 1
        else:
            crid_cut = re.sub(r'uk-crid~~3A~~2F~~2Fog.libertyglobal.com~~2F', '', row[1])
            provider =re.sub(r'~~2F.*', '', crid_cut)
            crid_cut = re.sub('.*~~2F', '', crid_cut)
            paid = re.sub(r'-.*', '', crid_cut)
            exec_date = re.sub(r' ', 'T', row[4])
            run_id = row[1]
            line_nb += 1
            data_to_write = [exec_date, run_id, provider, paid]
            paid_to_feed.append(paid)
            with open(report_name, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
                writer.writerow(data_to_write)
    print('Report generated: {}'.format(report_name))
    print('Feed this to OG: {}'.format(paid_to_feed))