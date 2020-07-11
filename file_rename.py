#python file_rename.py name
import os
import re
import sys
import shutil

if __name__ == '__main__':
    args = sys.argv
    num = 1
    arr = []
    child_dir = '/Volumes/Elements/dataset/StreetView/imgs/'
    for file_name in os.listdir(child_dir):
        if file_name.endswith('.jpg'):
            arr.append(file_name)
            shutil.move(child_dir + file_name, child_dir + args[1] + '_' + str(num) + '.jpg')
        num +=1
