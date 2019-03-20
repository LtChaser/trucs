import shutil
import os
import datetime
import sys
import time

x = 1

mod = input('Mod to play: \n >>')
#if

if mod == 'vc' or 'VC':
	dest = 'C:\\Users\\coust\\Documents\\Mount&Blade Warband Savegames - Backup\\VC'
	source = 'C:\\Users\\coust\\Documents\\Mount&Blade Warband Savegames\\Viking Conquest\\'
elif mod == 'pop' or 'POP':
	source = 'C:\\Users\\coust\\Documents\\Mount&Blade Warband Savegames\\Prophesy of Pendor V3.9.2\\'
	dest = 'C:\\Users\\coust\\Documents\\Mount&Blade Warband Savegames - Backup\\PoP'

while x:
    timestamp = datetime.datetime.now()
    for adi_dir, dirs, files in os.walk(source):
        for file in files:
            time   .sleep(60*5)
            source_path = source + file
            file_creation_time = os.path.getmtime(source_path)
            dest_path = dest + file + timestamp.strftime('-%Y%m%dT%H%M%S')
            if not os.path.exists(dest):
                try:
                    os.makedirs(os.path.dirname(dest))
                except:  # Guard against race condition
                    print('Directory could not be made')
            shutil.copyfile(source_path, dest_path)
            nowtime = datetime.datetime.now()
            print('[{}]: Save Backed-up'.format(nowtime))