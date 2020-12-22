# -*- coding:utf-8 -*-

import config
from tools.logger import logger
log = logger.get_logger()

# 提交订单的接口做测试
class Order():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/buy/add.html'

    def order(self, session):
        data = {
            'goods_id': 1,
            'stock': 2,
            'buy_type': 'goods',
            'address_id': 600,
            'payment_id': 1,
            'spec': '',
        }
        resp_order = session.post(self.url, data=data, headers=config.HEADERS)
        # 提取数据做数据关联   -->生成数据--数据放在公共区域
        # from config import JUMP_URL,IP   会以为jump_url只是一个被赋值的一个变量
        config.JUMP_URL = resp_order.json().get('data').get('jump_url')
        log.info(f'config.JUMP_URL的值是{config.JUMP_URL}')
        return resp_order


