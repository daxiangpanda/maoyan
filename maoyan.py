#!/usr/bin/env python
# encoding: utf-8

import urllib2
import csv
import datetime
import sys
import time
import random
import json
import osimport
reload(sys)
sys.setdefaultencoding("utf-8")

rowName = [u'showRate',u'movieId',u'subBoxOffice',u'releaseDay',u'showZero',u'dailyBoxOffice',u'movieName']

def dataprocess(html):
	content = json.loads(html)
	fileName = '/home/ted/python/maoyan.csv'
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
def main():
	begin = datetime.date(2011,01,01)
	end = datetime.date(2011,01,28)
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
