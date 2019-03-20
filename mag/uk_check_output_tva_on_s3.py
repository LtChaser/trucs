#!/usr/bin/python

import boto3
import botocore
from boto3 import client
import os.path
import xml.etree.ElementTree as ET
from lxml import etree
import json
import time
from datetime import datetime
import sys

start_time = time.time()

def remove_namespace(doc, namespace):
    """Remove namespace in the passed document in place."""
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]

def get_matching_s3_objects(bucket, prefix='', suffix=''):
    """
    Generate objects in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch objects whose key starts with
        this prefix (optional).
    :param suffix: Only fetch objects whose keys end with
        this suffix (optional).
    """
    s3 = client('s3',aws_access_key_id='AKIAJHGT4XIEEQCMVU3A',aws_secret_access_key='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')
    kwargs = {'Bucket': bucket}

    # If the prefix is a single string (not a tuple of strings), we can
    # do the filtering directly in the S3 API.
    if isinstance(prefix, str):
        kwargs['Prefix'] = prefix

    while True:

        # The S3 API response is a large blob of metadata.
        # 'Contents' contains information about the listed objects.
        resp = s3.list_objects_v2(**kwargs)

        try:
            contents = resp['Contents']
        except KeyError:
            return

        for obj in contents:
            key = obj['Key']
            if key.startswith(prefix) and key.endswith(suffix):
                yield obj

        # The S3 API is paginated, returning up to 1000 keys at a time.
        # Pass the continuation token into the next response, until we
        # reach the final page (when this field is missing).
        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break


def get_matching_s3_keys(bucket, prefix='', suffix=''):
    """
    Generate the keys in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch keys that start with this prefix (optional).
    :param suffix: Only fetch keys that end with this suffix (optional).
    """
    for obj in get_matching_s3_objects(bucket, prefix, suffix):
        yield obj['Key']



results = list(get_matching_s3_keys('piksel-lgi-assets',prefix='GB/prod/ondemand/TVA'))

s3 = boto3.resource('s3',aws_access_key_id='AKIAJHGT4XIEEQCMVU3A',aws_secret_access_key='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')

for KEY in results:
    if not os.path.isfile('{}/piksel-lgi-assets/{}'.format(os.path.dirname(os.path.abspath(__file__)),KEY)):
        try:
            s3.Bucket('piksel-lgi-assets').download_file(KEY, '{}/piksel-lgi-assets/{}'.format(os.path.dirname(os.path.abspath(__file__)),KEY))
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object {} does not exist.".format(KEY))
            else:
                raise
print("--- %s seconds ---" % (time.time() - start_time))
all_tva_files= os.listdir('{}/piksel-lgi-assets/GB/prod/ondemand/'.format(os.path.dirname(os.path.abspath(__file__))))
crid_per_tva_file = { 'crids': list() }
for file in all_tva_files:
        crid = str()
        crid_expiration = str()
        valid_asset = bool()
        ondemandproduct_count = 0
        ondemand = dict()
        parser = etree.XMLParser(ns_clean=True)
        if not os.path.isfile('{}/piksel-lgi-assets/GB/prod/ondemand/{}'.format(os.path.dirname(os.path.abspath(__file__)),file)):
            continue
        tree   = etree.parse('{}/piksel-lgi-assets/GB/prod/ondemand/{}'.format(os.path.dirname(os.path.abspath(__file__)),file), parser)
        root = tree.getroot()
        remove_namespace(root, 'urn:tva:metadata:2010')
        remove_namespace(root, 'urn:tva:mpeg7:2008')
        for element in root.iterfind('.//ProgramInformation'):
            crid_expiration = element.get('fragmentExpirationDate')
            crid = element.get('programId')
        for element in root.iterfind('.//OnDemandProgram'):
                ondemandproduct_count += 1
                for sub in element.iterfind('.//PurchaseItem'):
                        ondemand[ondemandproduct_count] = { 'start': sub.get('start'),
                                                            'end': sub.get('end') }
        for ondemandproduct_key,ondemandproduct_value in ondemand.items():
                start = datetime.strptime(ondemandproduct_value['start'],'%Y-%m-%dT%H:%M:%SZ')
                end = datetime.strptime(ondemandproduct_value['end'],'%Y-%m-%dT%H:%M:%SZ')
                if start < datetime.now() and datetime.now() < end:
                        valid_asset = True

        crid_per_tva_file['crids'].append( { 'crid': {
                                                'crid': crid,
                                                'tva_files': {
                                                    'filename': '{}'.format(file),
                                                    'fragmentExpirationDate': crid_expiration,
                                                    'OnDemandProducts': ondemand
                                                    }
                                                }
                                            }
                                        )
crid_list = dict()

for crid in crid_per_tva_file['crids']:
    valid_asset = bool()
    for ondemandproduct_key,ondemandproduct_value in crid['crid']['tva_files']['OnDemandProducts'].items():
        start = datetime.strptime(ondemandproduct_value['start'],'%Y-%m-%dT%H:%M:%SZ')
        end = datetime.strptime(ondemandproduct_value['end'],'%Y-%m-%dT%H:%M:%SZ')
        if start < datetime.now() and datetime.now() < end:
            valid_asset = True
    if crid['crid']['crid'] in crid_list:
                crid_list[crid['crid']['crid']]['tva_files'].update( {
                                len(crid_list[crid['crid']['crid']]['tva_files']) : {
                                    'valid_asset': valid_asset,
                                    'filename': crid['crid']['tva_files']['filename'],
                                    'fragmentExpirationDate': crid['crid']['tva_files']['fragmentExpirationDate'],
                                    'OnDemandProducts': crid['crid']['tva_files']['OnDemandProducts']
                                    }
                                }
                            )

    else:
        crid_list.update({ crid['crid']['crid'] : {
                            'tva_files': {
                                0 : {
                                    'valid_asset': valid_asset,
                                    'filename': crid['crid']['tva_files']['filename'], 
                                    'fragmentExpirationDate': crid['crid']['tva_files']['fragmentExpirationDate'],
                                    'OnDemandProducts': crid['crid']['tva_files']['OnDemandProducts']
                                    }
                                }
                            }
                            }
                            )
all_crid = { 'crids' : list() }
for crid in crid_list:
    latest_tva = str()
    for index, tva_file in crid_list[crid]['tva_files'].items():
        if latest_tva == '':
            latest_tva = index
        else:
            index_file = crid_list[crid]['tva_files'][index]['filename'].split('_')[2].split('.')[0].split('-')[0] 
            latest_file = crid_list[crid]['tva_files'][latest_tva]['filename'].split('_')[2].split('.')[0].split('-')[0]
            if int(index_file) > int(latest_file):
                latest_tva = index
    all_crid['crids'].append( { 'crid': {
                                    'crid': crid,
                                    'valid_asset': crid_list[crid]['tva_files'][latest_tva]['valid_asset'],
                                    'latest_tva' : latest_tva,
                                    'tva_files': crid_list[crid]['tva_files']
                                    }
                                }
                            )


print("--- %s seconds ---" % (time.time() - start_time))
with open('{}/output/uk_all_assets-{}.json'.format(os.path.dirname(os.path.abspath(__file__)),time.strftime('%Y%m%d')), 'w') as f:
        json.dump(all_crid, f)
print("--- %s seconds ---" % (time.time() - start_time))
