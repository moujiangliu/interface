# -*- coding:utf-8 -*-

import config
from tools.logger import logger
log = logger.get_logger()

class PayOrder():
    def __init__(self):
        '''
        这个支付接口是需要重定向,302的url是从提交订单的接口里面获取jump_url
        '''
        self.url = config.JUMP_URL
        log.info(f'self.url的值是{self.url}')

    def pay_order(self, session):
        # 对302接口进行处理,不让其重定向 allow_redirects=False
        resp_pay = session.get(self.url, allow_redirects=False)
        resp = session.get(resp_pay.headers['location'])
        return resp
