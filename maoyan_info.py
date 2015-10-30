#!/usr/bin/env python
# encoding: utf-8

import urllib2
def main():
    ed = []
    IDset = []
    for line in open('/home/ted/python/maoyan/maoyan.csv'):
        ID = line.split(',')[1]
        if ID in ed or ID == 'movieId':
            continue
        try:
            url = 'http://piaofang.maoyan.com/movie/baseinfo.json?movie='+str(ID)
            html = urllib2.urlopen(url,timeout = 5).read()
            html
        except Exception,e:
            continue
        ed.append(ID)
        print ed
if __name__ == '__main__':
        main()
