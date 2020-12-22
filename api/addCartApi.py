# -*- coding:utf-8 -*-

import config

class AddCart():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/cart/save.html'

    def add_cart(self, session):
        data = {
            'goods_id': 1,
            "stock": 1,
        }
        resp_cart = session.post(self.url, data=data, headers=config.HEADERS)
        return resp_cart

