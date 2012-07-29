#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test restful api
"""

import requests
import json

API_URL = "http://192.168.0.185:9500/j/"

def encode_json(o):
    return json.dumps(o, ensure_ascii=False)


class request():

    cookies = None
    
    def __init__(self, endpoint=None, method='get'):
        self.endpoint = endpoint
        self.method = method.lower()

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            params = func(*args, **kwargs) or {}
            url    = self.endpoint if self.endpoint else params.pop('url')
            is_login = True if url == 'login' else False
            #params = urllib.urlencode(params)
            url    = "%s%s" % (API_URL, url)
            
            print '\n>>> %s: %s' % (self.method.upper(), url)
            print '    PARAM: %s' % json.dumps(params, ensure_ascii=False)

            if self.method == 'get':
                r = requests.get(url, params=params, cookies=request.cookies)
                print '    STATUS: %d' % r.status_code
                print '    RETURN: %s' % encode_json(r.json)
            elif self.method == 'post':
                r = requests.post(url, params=params, cookies=request.cookies)
                print '    STATUS: %d' % r.status_code
                print '    RETURN: %s' % encode_json(r.json)
                if is_login:
                    cookie_dct = {}
                    for k, v in r.json.iteritems():
                        cookie_dct[k] = str(v)
                    request.cookies = cookie_dct
            else:
                print 'ERROR: Unkown HTTP Method: %s' % self.method
            return r.json
        return wrapped


class API:

    @request('login', method='post')
    def login(self, account, password):
        return {
            'account': account,
            'password': password
        }

    @request('pin/like', method="post")
    def user_like_pin(self, pid):
        return {
            'pid': pid
        }

    @request('pin/dislike', method="post")
    def user_dislike_pin(self, pid):
        return {
            'pid': pid
        }

    @request('account/edit', method="post")
    def account_edit(self, name, place, desc, email):
        return {
            'name': name,
            'place': place,
            'description': desc,
            'email': email,
        }

    @request('account/password/reset', method='post')
    def passwd_reset(self, old, new):
        return {
            'old_password': old,
            'new_password': new
        }
    
    @request('set_email', method='post')
    def set_email(self, uname, email):
        return {
            'user_name': uname,
            'em': email,
        }

    @request('board/4522/edit', method='post')
    def edit_board(self, name, desc):
        return {
            'name': name,
            'desc': desc
        }

    @request('board/6484/delete', method='post')
    def del_board(self):
        return {}

    @request('invite/validate', method='post')
    def check_invite(self, q, a):
        return {
            'question': q,
            'answer': a
        }

    @request('board/follow', method='post')
    def follow_board(self, bid):
        return {
            'board_id': bid,
        }

    @request('board/unfollow', method='post')
    def unfollow_board(self, bid):
        return {
            'board_id': bid,
        }

    @request('pin/51781/delete', method='post')
    def del_pin(self):
        return {}

    @request('feedback', method='post')
    def feedback(self, content):
        return {
            'content': content
        }

    @request('account/pic/upload', method='post')
    def upload_avatar(self):
        return {
            'content': ''
        }

    @request('account/register', method='post')
    def register(self, username, mail, password):
        return {
            'username': username,
            'mail': mail,
            'password': password
        }

    @request('pin/122648/comment', method='post')
    def post_pin_comment(self, content):
        return {
            'content': content,
        }

    @request('pin/122648/comment', method='get')
    def get_pin_comment(self, page, length):
        return {
            'page': page,
            'length': length
        }


    @request('comment/520/delete', method='post')
    def delete_comment(self):
        return {}


    @request('wantbe/create', method='post')
    def add_wantbe(self, wid, wtype):
        return {
            'wid': wid,
            'wtype': wtype
        }

    @request('peoples/follow', method='post')
    def follow_peoples(self, ids):
        return {
            'ids': ids,
        }

    @request('peoples/unfollow', method='post')
    def unfollow_peoples(self, ids):
        return {
            'ids': ids,
        }

if __name__ == '__main__':
    t = API()
    #t.register('上海人', '1@2.com', 'y')
    t.login('1-1@1.com', '111111')
    #t.post_pin_comment('Fuck !!!')
    #t.get_pin_comment(1, 10)
    #t.user_like_pin(147698)
    #t.delete_comment()
    #t.user_dislike_pin(2283715)
    #t.account_edit('panda', 'SH', 'Panda if panda, love is love', '1')
    #t.passwd_reset('1', '1')
    #t.set_email('Panda', '1')
    #t.edit_board('', '中文很不错嘛')
    #t.del_board()
    #t.check_invite(u'进入网站的邀请码？', u'你猜')
    #t.unfollow_board(2778)
    #t.follow_board(2778)
    #t.del_pin()
    #t.upload_avatar()
    #t.add_wantbe(147730, 1)
    t.follow_peoples('897,898')
    t.unfollow_peoples('897,898')
