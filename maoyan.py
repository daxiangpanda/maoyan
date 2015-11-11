#!/usr/bin/env python
# encoding: utf-8

import urllib2
import csv
import datetime
import sys
import time
import json
import os
import pickle
reload(sys)
sys.setdefaultencoding("utf-8")

rowName = [u'showRate',u'movieId',u'subBoxOffice',u'releaseDay',u'boxRate'u'showZero',u'dailyBoxOffice',u'movieName']

def dataprocess(html):
    content = json.loads(html)
    fileName = 'E:\maoyan-master\maoyan.csv'
    if os.path.exists(fileName):
        mode = 'ab'
    else:
        mode = 'wb'
    csvfile = file(fileName,mode)
    writer = csv.writer(csvfile)
    if mode == 'wb':
        writer.writerow([name.encode('utf8') for name in rowName])
    for i in content["data"]:
        info = [i["showRate"],i["movieId"],i["sumBoxOffice"],i["releaseDay"],i["boxRate"],i["showZero"],i["dailyBoxOffice"],i["movieName"]]
        writer.writerow([str(d).encode('utf8') for d in info])
    csvfile.close()

def getbegin_end():
    with open('date','r') as f:
        a = f.read()
    a = pickle.loads(a)
    begin_1 = a['end']
    end_1 = datetime.datetime.now().date()
    a['begin'] = a['end']
    a['end'] = datetime.datetime.now().date()
    with open('date','w+') as f:
        f.write(pickle.dumps(a))
    return begin_1, end_1

def main():
    begin,end = getbegin_end()
    timeset = []
    timeremain = []
    for i in range((end-begin).days + 1):
        day = begin + datetime.timedelta(days = i)
        timeset.append(day)
    print timeset
    while timeset:
        for i in timeset:
            try:
                url = 'http://piaofang.maoyan.com/history/date/box.json?date='+str(i)+'&cnt=10'
                html = urllib2.urlopen(url,timeout = 5).read()
                #print html
                dataprocess(html)
                time.sleep(0.5)
                print i
            except Exception,e:
                timeremain.append(i)
                continue
        timeset = timeremain
        timeremain = []

if __name__ == '__main__':
    main()
