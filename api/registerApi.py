# -*- coding:utf-8 -*-


import config


class RegisterApi():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/user/reg.html'

    def registerApi(self, session, data):
        resp_reg = session.post(self.url, data=data, headers=config.HEADERS)
        return resp_reg
