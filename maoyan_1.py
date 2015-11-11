__author__ = '31351'
#!/usr/bin/env python
# encoding: utf-8
import urllib2
import csv
import datetime
import sys
import time
import json
import os
reload(sys)
sys.setdefaultencoding("utf-8")

def dataprocess(html):
    content = json.loads(html)
    fileName = r'E:\maoyan-master\maoyan_1.csv'
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
    
def datetrans(str):
    return datetime.date(int(str.split("-")[0]),int(str.split("-")[1]),int(str.split("-")[2]))

def date(begin, end):
    begin = datetrans(begin)
    end = datetrans(end)
    timeset = []
    for i in range((end-begin).days + 1):
        day = begin+datetime.timedelta(days = i)
        timeset.append(day)
    return timeset

def main(timeset):
    print timeset
    timeremain = []
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
    return 0

str1 = raw_input("begin date:")
str2 = raw_input("end date")
timeset = date(datetrans(str1),datetrans(str2))
main(timeset)