# -*- coding:utf-8 -*-

from config import IP,HEADERS
import requests
from tools.logger import logger

log = logger.get_logger()


class MtxLogin(object):
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'

    log.info('登录参数化接口')
    def login(self, session, data):
        res_login = session.post(self.url, data=data, headers=HEADERS)
        return res_login

    log.info('正向登录')
    def login_success(self, session):
        '''
        发请登录成功的请求
        :param session:
        :return:
        '''
        data = {'accounts':'moujiang', 'pwd':'moujiang'}
        res_login = session.post(self.url, data=data, headers=HEADERS)
        return res_login

