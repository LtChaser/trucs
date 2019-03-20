import os
import time, datetime
from openpyxl import load_workbook
import shutil
import sys

# C.O

# file_path = 'O:\eTVStudio\Ziggo NL\Banners\\2018\\Banner planning_2018 - JUNE 2018- RPO MK.XLSX'
# wb = load_workbook(filename = file_path)
# sheet_ranges = wb['banners'] #name of sheet itself
# print(sheet_ranges['E1102'].value)
def user_input(value_type, x):
    loop_param = True
    while loop_param:
        value_to_return = input('Enter {} value {} or type "Done" to proceed').format(value_type, x)
        if value_to_return == 'Done' or 'done':
            loop_param = False
        else:
            return value_to_return

def determine_working_directory():

    now = datetime.datetime.now()
    weeknb = (now.isocalendar()[1])
    #weeknb = '47'# Testing purpose
    year = now.year
    working_dir = 'O:\eTVStudio\Ziggo NL\Banners\{}\Week {}\\'.format(year, weeknb)
    #working_dir = 'C:\Banner_test_edit\{}\Week {}\\'.format(year, weeknb)
    return working_dir


def create_lab_directory():

    today_date = time.strftime('%Y%m%d')
    dir_path = 'C:\Banner_test_edit\\{}\\'.format(today_date) #temp_path
    if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            os.makedirs(dir_path + 'Radio\\Images')
            os.makedirs(dir_path + 'TV Guide\\Images')
            os.makedirs(dir_path + 'TV Search\\Images')
    return dir_path


def process_data(image_dir, lab_dir, asset_dict, title, crid):
    bmp_dir = image_dir + 'Images\\' + '239x53\\'
    jpg_dir = image_dir + 'Images\\' + '300x58\\'
    bmp_files = os.listdir(bmp_dir)
    jpg_files = os.listdir(jpg_dir)
    i = 0
    y = 0
    j = 0
    next_xml = [0]

    while j < len(bmp_files) - 1:
        next_xml.insert(j, j+1)
        j += 1

    try:

        for file in bmp_files:
            bmp_path = bmp_dir + file
            bmp_dest_path = '{}TV Guide\\Images\\NL_TVOD_0{}.bmp'.format(lab_dir, i)
            shutil.copyfile(bmp_path, bmp_dest_path)
            build_xml_tvguide(lab_dir + "TV Guide", i, title, crid, next_xml[i])
            i += 1
        for file in jpg_files:
            jpg_path = jpg_dir + file
            jpg_dest_path1 = '{}Radio\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
            jpg_dest_path2 = '{}TV Search\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
            shutil.copyfile(jpg_path, jpg_dest_path1)
            build_xml_radio(lab_dir + "Radio", y, title, crid, next_xml[y])
            shutil.copyfile(jpg_path, jpg_dest_path2)
            build_xml_tvsearch(lab_dir + "TV Search", y, title, crid, next_xml[y])
            y += 1
    except Exception as e:
        print("Exception: {}".format(e))
        print("Did you input enough crid and titles?")

def build_xml_tvguide(path, i, title, crid, next_xml):
    xml_format = '<advert>\n' \
                 '<image href="http://172.18.20.17/NL/spinnaker/tvguide/TVG02/Images/NL_TVOD_0{}.bmp"/>\n' \
                 '<label value="{}"/>\n' \
                 '<duration value="6000"/>\n' \
                 '<action name="launchHyperlink">\n' \
                 '<parameter name="ondemand" value="itv://Ondemand/vod2/2.0.11/PackageLink?crid={}&amp;adultContent=none&amp;theme=Default"/>\n' \
                 '</action>\n' \
                 '<next href="http://172.18.20.17/NL/spinnaker/tvguide/TVG02/xml{}"/>\n' \
                 '</advert>'.format(i, title, crid, next_xml)
    with open(path + '\\xml{}'.format(i), 'w') as f:
        f.write(xml_format)
        f.close()


def build_xml_tvsearch(path, i, title, crid, next_xml):
    xml_format = '<advert>\n' \
                 '<image href="http://172.18.20.17/NL/spinnaker/tvsearch/tvsearch_mainmenu/Images/NL_TVOD_0{}.jpg"/>\n' \
                 '<label value="{}"/>\n' \
                 '<duration value="6000"/>\n' \
                 '<action name="launchHyperlink">\n' \
                 '<parameter name="ondemand" value="itv://Ondemand/vod2/2.0.11/PackageLink?crid={}&amp;adultContent=none&amp;theme=Default"/>\n' \
                 '</action>\n' \
                 '<next href="http://172.18.20.17/NL/spinnaker/tvsearch/tvsearch_mainmenu/xml{}"/>\n' \
                 '</advert>'.format(i, title, crid, next_xml)
    with open(path + '\\xml{}'.format(i), 'w') as f:
        f.write(xml_format)
        f.close()

def build_xml_radio(path, i, title, crid, next_xml):
    xml_format = '<advert>\n' \
                 '<image href="http://172.18.20.17/NL/spinnaker/radio/RIGHTBOTTOM_SMALL/Images/NL_TVOD_0{}.jpg"/>\n' \
                 '<label value="{}"/>\n' \
                 '<duration value="6000"/>\n' \
                 '<action name="launchHyperlink">\n' \
                 '<parameter name="ondemand" value="itv://Ondemand/vod2/2.0.11/PackageLink?crid={}&amp;adultContent=none&amp;theme=Default"/>\n' \
                 '</action>\n' \
                 '<next href="http://172.18.20.17/NL/spinnaker/radio/RIGHTBOTTOM_SMALL/xml{}"/>\n' \
                 '</advert>'.format(i, title, crid, next_xml)
    with open(path + '\\xml{}'.format(i), 'w') as f:
        f.write(xml_format)
        f.close()

def user_input():
    i = 0
    x = 1
    asset_dict = {}
    while True:
        title = input('Enter Title value {} or type "Done" to proceed: '.format(x))
        if title != 'Done':
            crid = input('Enter Crid value {} or type "Done" to proceed: '.format(x))
            if crid != "Done":
                asset_dict.update({title: crid})
                #print(asset_dict.keys, asset_dict[title]) # COMES BACK TO THIS. DICT NOT ACCESSIBLE IN THIS FASHION
                #print(asset_dict[title]) # COMES BACK TO THIS. DICT NOT ACCESSIBLE IN THIS FASHION
                i +=1
                x += 1
                continue
            else:
                break
        else:
            break
    return asset_dict


##########################################
##### Duplicate Function for testing #####
##########################################
def process_data_test(image_dir, lab_dir, asset_dict, title_list, crid_list):
    bmp_dir = image_dir + 'Images\\' + '239x53\\'
    jpg_dir = image_dir + 'Images\\' + '300x58\\'
    bmp_files = os.listdir(bmp_dir)
    jpg_files = os.listdir(jpg_dir)
    i = 0
    y = 0
    j = 0
    next_xml = [0]
    while j < len(bmp_files) - 1:
        next_xml.insert(j, j+1)
        j += 1

    print(title_list)
    try:
        # while i < len(bmp_files):
        #     for file in bmp_files:
        #         title_split = title_list[i].split() #i is exhausted
        #         if title_split[0] in file:
        #             print("it is")
        #             bmp_path = bmp_dir + file
        #             bmp_dest_path = '{}TV Guide\\Images\\NL_TVOD_0{}.bmp'.format(lab_dir, i)
        #             shutil.copyfile(bmp_path, bmp_dest_path)
        #             build_xml_tvguide(lab_dir + "TV Guide", i, title_list[i], crid_list[i], next_xml[i])
        #             i += 1
        #         else:
        #             i -= 1        while i < len(bmp_files):
        for file in bmp_files:
            for title in title_list:
                title_split = title.split() #i is exhausted
                if title_split[0] in file:
                    print("it is")
                    bmp_path = bmp_dir + file
                    bmp_dest_path = '{}TV Guide\\Images\\NL_TVOD_0{}.bmp'.format(lab_dir, i)
                    shutil.copyfile(bmp_path, bmp_dest_path)
                    build_xml_tvguide(lab_dir + "TV Guide", i, title_list[i], crid_list[i], next_xml[i])
                    i += 1

        while y < len(jpg_files):
            for file in jpg_files:
                for title in title_list:
                    title_split = title.split()
                    if title_split[0] in file:
                        jpg_path = jpg_dir + file
                        jpg_dest_path1 = '{}Radio\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
                        jpg_dest_path2 = '{}TV Search\\Images\\NL_TVOD_0{}.jpg'.format(lab_dir, y)
                        shutil.copyfile(jpg_path, jpg_dest_path1)
                        shutil.copyfile(jpg_path, jpg_dest_path2)
                        build_xml_radio(lab_dir + "Radio", y, title_list[y], crid_list[y], next_xml[y])
                        build_xml_tvsearch(lab_dir + "TV Search", y, title_list[y], crid_list[y], next_xml[y])
                        y += 1
    except Exception as e:
        print("Exception: {}".format(e))
        print("Did you input enough crid and titles?")


#######################################

asset_dict = user_input()
working_dir = determine_working_directory()
lab_dir = create_lab_directory()
title_list = []
crid_list = []
for title, crid in asset_dict.items():
    title_list.append(title)
    crid_list.append(crid)
process_data_test(working_dir, lab_dir, asset_dict, title_list, crid_list)
#process_data_test(working_dir, lab_dir, asset_dict)

