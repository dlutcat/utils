#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################
# 爬取指定用户最新5条腾讯微播     #
###################################

import urllib2, urllib, time

END_POINT = 'http://t.qq.com/'

HEADERS = {
  'Cookie': ''
}

def fetch_page(user):
  request = urllib2.Request( url=END_POINT+user, headers=HEADERS)
  resp = urllib2.urlopen(request)
  html = resp.read()
  resp.close();
  return html

def soup_tweets(user='XXX'):
  from BeautifulSoup import BeautifulSoup, Tag
  page = fetch_page(user)
  start_time = time.time()
  soup = BeautifulSoup(page)
  tweets = soup.find(id='talkList').findAll('li')[:5]

  for t in tweets:
    content = t.find(attrs={ 'class': 'msgCnt'})
    pub_time = t.find(attrs={ 'class': 'time' })

    if pub_time:
      print 'Time: ' + pub_time.getText()

    if content:
      print 'Content: ',
      for c in content.contents:
        if isinstance(c, Tag):
          if c.has_key('title'):
            print '[%s]' % c['title'],
          else:
            print c.getText(),
        else:
          print c,
      print 
      print '------------------------------------------'

def query_tweets(user='XXX'):
  from pyquery import PyQuery as py
  page = fetch_page(user)
  start_time = time.time()
  py_page = py(page )
  print py_page('#talkList')
  print 'PyQuery Time: %s' % str(time.time() - start_time)

if __name__ == '__main__':
  soup_tweets()
  #query_tweets()
