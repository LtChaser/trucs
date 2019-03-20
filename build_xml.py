import os
import time, datetime
from openpyxl import load_workbook
import shutil
import sys

def build_xml(path, img_nb, title, crid, next_xml):
    xml_format = '<advert>\n' \
                 '<image href="http://172.18.20.17/NL/spinnaker/tvsearch/tvsearch_mainmenu/Images/NL_TVOD_0{}.jpg"/>\n' \
                 '<label value="{}"/>\n' \
                 '<duration value="6000"/>\n' \
                 '<action name="launchHyperlink">\n' \
                 '<parameter name="ondemand" value="itv://Ondemand/vod2/2.0.11/PackageLink?crid={}&amp;adultContent=none&amp;theme=Default"/>\n' \
                 '</action>\n' \
                 '<next href="http://172.18.20.17/NL/spinnaker/tvsearch/tvsearch_mainmenu/xml{}"/>\n' \
                 '</advert>'.format(img_nb, title, crid, next_xml)
    with open(path + '\\xml{}'.format(next_xml), 'w') as f:
        f.write(xml_format)
        f.close()


def process_data(image_dir, lab_dir, asset_dict, title, crid):
    bmp_dir = image_dir + 'Images\\' + '239x53\\'
    jpg_dir = image_dir + 'Images\\' + '300x58\\'
    bmp_files = os.listdir(bmp_dir)
    jpg_files = os.listdir(jpg_dir)
    i = 0
    y = 0
    next_xml = [1, 2, 0]
    for file in bmp_files:
        bmp_path = bmp_dir + file
        bmp_dest_path = '{}TV Guide\\Images\\NL_TVOD_0{}.bmp'.format(lab_dir, i)
        shutil.copyfile(bmp_path, bmp_dest_path)
        build_xml(lab_dir + "TV Guide", i, title[i], crid[i], next_xml[i])
        i += 1

def user_input():
    i = 0
    x = 1
    asset_dict = {}
    while True:
        title = input('Enter Title value {} or type "Done" to proceed: '.format(x))
        if title != 'Done':
            print(title)
            crid = input('Enter Crid value {} or type "Done" to proceed: '.format(x))
            if crid != "Done":
                asset_dict.update({title: crid})
                #print(asset_dict.keys, asset_dict[title]) # COMES BACK TO THIS. DICT NOT ACCESSIBLE IN THIS FASHION
                print(asset_dict[title]) # COMES BACK TO THIS. DICT NOT ACCESSIBLE IN THIS FASHION
                i +=1
                x += 1
                continue
            else:
                break
        else:
            break
    return asset_dict


image_dir = 'O:\eTVStudio\Ziggo NL\Banners\\2018\Week 29'
lab_dir = 'C:\Banner_test_edit\\20180821\TV Guide'
asset_dict = user_input()
for key, value in asset_dict.items():
    process_data(lab_dir, lab_dir, asset_dict, key, value)