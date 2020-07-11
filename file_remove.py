#python file_remove.py num
import os
import re
import sys
import shutil

if __name__ == '__main__':
    args = sys.argv
    arr = []
    child_dir = '/Volumes/Elements/dataset/StreetView/imgs/'
    for file_name in os.listdir(child_dir):
        if file_name.endswith('.jpg'):
            basename = os.path.splitext(os.path.basename(file_name))[0]
            number   = basename.split('_')
            if (int(number[1]) % int(args[1])) == 0:
                os.remove(child_dir + file_name)
