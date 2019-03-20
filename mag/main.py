#!/usr/bin/python2
import tva_retrieval.uk_check_s3_tva
import mag_calls.find_product_ids
import os
import time

def main():

    #output_json = '/home/nrw/'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    uk_check_s3 = tva_retrieval.uk_check_s3_tva.CheckS3Tva(base_dir)
    crid_dict = uk_check_s3.main_parse_s3()
    magcalls = mag_calls.find_product_ids.FindMissingProductIds(crid_dict, base_dir)
    urls = magcalls.url_json()
    magcalls.magcall(urls)



if __name__=="__main__":
    main()
