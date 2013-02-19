#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

def translate(word):

    URL='http://dict.cn/mini.php'
    params = {
        'q': word,
        'utf8': 'true'
    }
    req = urllib2.Request(
        url=URL,
        data=urllib.urlencode(params)
    )
    resp = urllib2.urlopen(req).read()

    soup = BeautifulSoup(resp)
    
    print
    print '========== %s =========' % word
    print
    print '解释 =======>'
    defs = soup.find('def').renderContents()
    segs = defs.split('\n')
    for i,s in enumerate(segs):
        print '(%s) %s' % ( i+1, s )
    print '例句 =======> '

    sents = soup.findAll('sent')

    for x,sent in enumerate(sents):
        orig = sent.find('orig')
        trans = sent.find('trans')
        print '[ORIG] %s' % clearHtml(orig.renderContents())
        print '[TRAN] %s' % clearHtml(trans.renderContents())
    print

def clearHtml(s):
    if s is None:
        return
    else:
        return s.replace('&lt;em&gt;', '').replace('&lt;/em&gt;', '')

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: %s [word]' % sys.argv[0]
        sys.exit(0)

    translate(sys.argv[1])
