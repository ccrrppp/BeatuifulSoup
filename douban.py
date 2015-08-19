# BeatuifulSoup
#豆瓣电影排名
# _*_ coding: utf-8 _*_
__author__ = 'Administrator'

import sys
import urllib2
from BeautifulSoup import BeautifulSoup
import HTMLParser
import re
from bs4 import BeautifulSoup

def crawl(url):
	page = urllib2.urlopen(url)
	contents = page.read()
	soup = BeautifulSoup(contents)
	print(u'豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数')
	for tag in soup.find_all('div', class_='item'):
		m_order = int(tag.find('em').get_text())
		m_name = tag.a.get_text()
		m_year = tag.span.get_text()
		for y in tag.find_all('em'):
			if y.get_text() != m_order :
				score =  y.get_text()
		'''m_rating_num =  int(tag.find_all('em').get_text())'''
		la= []
		for n in tag.find_all('span'):
			la.append(n)

		if len(la[4].get_text() ) <= 4:
			m_rating_num = la[5].get_text()
		else:
			m_rating_num = la[4].get_text()
		print("%s %s %s %s %s" % (m_order, m_name, m_year, score, m_rating_num))
		
if __name__ == '__main__':
	crawl('http://movie.douban.com/top250?format=text')
