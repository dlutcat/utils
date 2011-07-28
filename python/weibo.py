#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from weibopy.auth import OAuthHandler, BasicAuthHandler
from weibopy.api import API

class Test(unittest.TestCase):
    
    consumer_key= "1935104735"
    consumer_secret ="c32c9e8eae461711b367132a38b44d79"
    
    def __init__(self):
      """ constructor """
    
    def getAtt(self, key):
        try:
            return self.obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def getAttValue(self, obj, key):
        try:
            return obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def auth(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth_url = self.auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verifier = raw_input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        self.api = API(self.auth)
    def basicAuth(self, source, username, password):
        self.authType = 'basicauth'
        self.auth = BasicAuthHandler(username, password)
        self.api = API(self.auth,source=source)        
    def setToken(self, token, tokenSecret):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.setToken(token, tokenSecret)
        self.api = API(self.auth)
    
    def post(self, message):
        if isinstance(message, unicode):
            message = message.encode("utf-8")
        status = self.api.update_status(status=message)
        self.obj = status
        id = self.getAtt("id")
        text = self.getAtt("text")
        print "post---"+ str(id) +":"+ text

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s [tweet]' % sys.argv[0]
        sys.exit(0)
    test = Test()
    test.setToken("83d282816b58ea73a32b414396d1fa62", "1c39049b32813c26d96f5a5ab5ff48ef")
    test.post(sys.argv[1])
