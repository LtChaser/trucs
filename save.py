import shutil
import os
import datetime
import sys
import time

x = 1
source = 'C:\\adi_tmp_dir\\mock_dir\\'
dest = 'C:\\Save_test\\'

while x:
    timestamp = datetime.datetime.now()
    for adi_dir, dirs, files in os.walk(source):
        for file in files:
            sys.wait(60*5)
            source_path = source + file
            file_creation_time = os.path.getmtime(source_path)
            print(file_creation_time)
            dest_path = dest + file + timestamp.strftime('-%Y%m%dT%H%M%S')
            print(dest_path)
            if not os.path.exists(dest_path):
                try:
                    os.makedirs(os.path.dirname(dest_path))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            shutil.copyfile(source_path, dest_path)