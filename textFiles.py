import os
import sys
import shutil
from PIL import Image
from collections import defaultdict
import filecmp
import random
import string
import hashlib
import time


def isTextFile(f):
    return f.lower().endswith(('.txt', '.docx'))

def cmpHash(text1):
    hash1 = hashlib.md5()
    hash1.update(text1)
    hash1 = hash1.hexdigest()
    return hash1

if len(sys.argv) != 3:
    print "Error !!! Correct usage : python textFiles.py <Directory for text> <Directory for uniques>"
    exit()

# Removing "/" from the end of the source directory
if sys.argv[1].endswith('/'):
    sys.argv[1] = sys.argv[1][:-1]

# Adding "/" at the end of the destination directory
if sys.argv[2].endswith('/') == 0:
    sys.argv[2] += "/"

hash_value = {}
similar_file_list = defaultdict(list)
# files = [f for f in os.listdir(sys.argv[1])]
# files = [sys.argv[1] + f for f in files]
for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if len(file) == 0:
            continue
        f = root + "/" + file
        x = f
        if not isTextFile(x):
            continue
        # print file[0], "hey"
        hash_value[file[0]] = 0

unique_files = 0
for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        f = root + "/" + file
        x = f
        if not isTextFile(x):
            continue
        # print x
        if hash_value[file[0]] == 1:
            # print file[0], "asim"
            continue
        # print file, "seeeeee"
        hash_value[file[0]] = 1
        flag = 1
        cnt = 0
        for file1 in files:
            if not isTextFile(file1):
                # print "hi"
                continue
            if filecmp.cmp(root + '/' + file, root + '/' + file1):
                # print root + '/' + file, root + '/' + file1, "ajay"
                hash_value[file1[0]] = 1
                # print file, file1, hash_value[file[0]], hash_value[file1[0]]
        #         cnt += 1
        #         if cnt >= 2:
        #             flag = 0
        #             break
        #         if flag == 0:
        #             break

        if flag == 1:
            # print file, "yes ankesh"
            if not os.path.exists(sys.argv[2]):
                os.makedirs(sys.argv[2])
            shutil.copyfile(f, sys.argv[2] + file)
            unique_files += 1

print unique_files, " files were found unique"
        # Image and it's hash
        # print f, " --> ", hash_value[f]


unique_files = 0
