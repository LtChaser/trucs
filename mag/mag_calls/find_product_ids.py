#!/usr/bin/python
import json
import urllib2
import time
import csv
import mag_calls.key_access


class FindMissingProductIds:

    # input_file = '/home/dtv/input/valid_assets.json'
    def __init__(self,crid_dict, base_dir):
        self.dict = crid_dict
        self.base_dir = base_dir

    def url_json(self):
        i = 0
        url_list = []
    
        #data = open(self.f).read()
        d = self.dict
        crids_lenghth = len(d["crids"])
        while i < crids_lenghth:
            crid = d["crids"][i]["crid"]["crid"]
            url = 'https://feed-lgiprod.sequoia.piksel.com/f/lgi-gb-prod-master/orion-default-mediaitems?withAlternativeIdentifiers=crid:{}'.format(crid)
            url_list.append(url)
            i += 1
        return url_list

    def magcall(self, urls):
        failed_url = 0
        tested_assets = 0
        missing_p_id = 0
        nb_of_valid = 0
        nb_of_invalid = 0
        nowtime = time.strftime("%Y%m%dT%H%M%S")
    

        csv_path = '{}/output/all_tested_assets-{}.csv'.format(self.base_dir, nowtime)
        with open(csv_path, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(
                ['TITLE', 'CRID', 'parentID', 'rootID', 'mediaGroupId', 'currentProductID', 'availabilityEndAt'])
        for url in urls:
            time.sleep(0.5)
            try:
                json_data = urllib2.urlopen(url).read()
                data = json.loads(json_data)
                keys = mag_calls.key_access.Keys(data, url)
                availabilityEndDate = keys.availabilityEndDate()
                if nowtime < availabilityEndDate:
                    nb_of_valid += 1
                    # Loop here if necessary: for d['contents'][i]['bla']
                    title = keys.title()
                    crid = keys.crid()
                    parentId = keys.parentId()
                    rootId = keys.rootId()
                    mediaGroupId = keys.mediaGroupId()
                    cProductIds = keys.currentProductIds()
    
                    metadata = [title, crid, parentId, rootId, mediaGroupId, cProductIds, availabilityEndDate]
    
                    with open(csv_path, 'a') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                            lineterminator='\n')
                        writer.writerow(metadata)
                    if not cProductIds:
                        missing_p_id += 1
                else:
                    nb_of_invalid += 1
    
            except:
                # print("URL could not be loaded: ", url)
                failed_url += 1
        print("Job done.")
        print(missing_p_id, " assets missing Product ID for ", nb_of_valid, " assets tested")
        print(nb_of_invalid, " expired assets were found")
        print(failed_url, " API calls were not sucessfull")
    




# check product is available under currentProductIds
# mediaGroupId,  parentId and rootId
# Seasons ex
# https://web-api-pepper.horizon.tv/oesp/v3/GB/eng/web/mediaitems?byParentId=crid:~~2F~~2Fog.libertyglobal.com~~2FCNW~~2F12001575&sort=seriesEpisodeNumber|ASC,secondaryTitle|ASC&byMediaType=Episode
# https://feed-lgiprod.sequoia.piksel.com/f/lgi-gb-prod-master/orion-default-mediaitems?withAlternativeIdentifiers=crid:crid://og.libertyglobal.com/CNW/PAID0000000001541302
