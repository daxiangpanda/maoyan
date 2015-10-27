#!/usr/bin/env python
# encoding: utf-8


import urllib
import csv
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider():
	def __init__(self,date = '2015-10-25'):
		self.url = 'http://piaofang.maoyan.com/history/date/box.json?date='+date+'&cnt=10'
		self.rowName = []
def get_info(content):
    rank = soup.find('span','top250-no').get_text().split('.')[1]
    name = soup.find('span',property="v:itemreviewed").get_text()
    year = soup.find('span','year').get_text()[1:5].encode('utf8')
    try:
        intro = soup.find('span','all hidden').get_text().replace(' ','')
    except:
        intro = soup.find_all(property="v:summary")[0].get_text().replace(' ','')
    intro = intro.replace(r'\n','')
    score = soup.find('strong','ll rating_num').get_text()
    info = [rank,name,year,score,intro]
    for i in range(len(info)):
        info[i] = info[i].encode('utf8')
    print type(info[0])
    return info
f = open(r'/home/ted/python/douban/豆瓣top250.txt','w+')
for i in range(0,250,25):
    html = (urllib.urlopen('http://movie.douban.com/top250?start=%d&filter=&type='%i).read()).replace('\n','')
    #html = html.replace(' ','')
    pattern = r'<a href="http://movie.douban.com/subject/\d{7}/">'
    tags = re.findall(pattern,html)
    for tag in tags:
        url = tag.split('"')[1]
        req = urllib2.Request(url)
        try:
            content = urllib2.urlopen(req).read().decode("utf-8")
        except urllib2.URLError,e:
            f.write('你寻找的电影不存在，错误码'+str(e.code))
        info = get_info(content)
        s = "电影排名：" + info[0] + "名称:" + info[1] + "上映时间:" + info[2] + "评分" + info[3] + "\n" + "intro:" + info[4]
        insert(info)
        print "已写入" + s
        f.write(s)
    conn.commit()
cur.close()
conn.close()
f.close()
