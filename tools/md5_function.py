# -*- coding:utf-8 -*-

import base64
import hashlib

class Secret(object):
    '''
    实现各种加密方式
    '''
    def __init__(self, string):
        self._string = string.encode('utf-8')

    def md5(self):
        '''
        md5加密方法
        :return:
        '''
        try:
            sign = hashlib.md5(self._string).hexdigest()
            return sign
        except:
            return False

    def sha1(self):
        '''
        实现sha1的加密方法
        :return:
        '''
        try:
            sign = hashlib.sha1(self._string).hexdigest()
            return sign
        except:
            return False

    def base64encode(self):
        '''
        实现一个base64 encode的方法封装
        '''
        try:
            sign = base64.b64encode(self._string).decode('utf-8')
            return sign
        except:
            return False

    def base64decode(self):
        '''
        base64 decode的方法封装 (解码)
        :return:
        '''
        try:
            sign = base64.b64decode(self._string).decode('utf-8')
            return sign
        except:
            return False





