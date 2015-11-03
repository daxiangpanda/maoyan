__author__ = '31351'

import csv
import os
import urllib

info = {}
with open('E:\maoyan-master\maoyan_info.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        info[row[3]] = row[2]

for url in info.keys():
    name = info[url].decode('utf8') + '.' + url.split('.')[-1]
    url = url.replace('w.h','165.220')
    path = 'E:\\maoyan-master\\post\\'
    try:
        urllib.urlretrieve(url, path+name)
    except BaseException, e:
        print e
    print name
