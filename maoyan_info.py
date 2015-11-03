#!/usr/bin/env python
# encoding: utf-8
import os
import urllib2
import json
import csv
rowName = [u'category',u'drama',u'name',u'image',u'stars',u'director',u'wishNum',u'score',u'version',u'scoreNum',u'duration',u'id',u'releaseTime']
def dataprocess(html):
    content = json.loads(html)
    fileName = '/home/lxz/python/maoyan/maoyan_info.csv'
    if os.path.exists(fileName):
        mode = 'ab'
    else:
        mode = 'wb'
    csvfile = file(fileName,mode)
    writer = csv.writer(csvfile)
    if mode == 'wb':
        writer.writerow([name.encode('utf8') for name in rowName])
    for i in content["data"]:
        info = [i["category"],i["drama"],i["name"],i["image"],i["stars"],i["director"],i["wishNum"],i["score"],i["version"],i["scoreNum"],i["duration"],i["id"],i["releaseTime"]]
        writer.writerow([str(d).encode('utf8') for d in info])
    csvfile.close()

def main():
    ed = []
    IDset = []
    IDremain = []
    for line in open('/home/lxz/python/maoyan/maoyan.csv'):
        ID = line.split(',')[1]
        if ID in ed or ID == 'movieId':
            continue
        url = 'http://piaofang.maoyan.com/movie/baseinfo.json?movie='+str(ID)
        html = urllib2.urlopen(url,timeout = 5).read()
        dataprocess(html)
        print ID
        ed.append(ID)
        #except Exception,e:
            #print e
            #continue
            
if __name__ == '__main__':
        main()
