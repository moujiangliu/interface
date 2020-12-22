# -*- coding:utf-8 -*-

import config

class DeleteCart():
    def __init__(self):
        self.url_cart = config.IP + '/mtx/index.php?s=/index/cart/index.html'
        self.url = config.IP + '/mtx/index.php?s=/index/cart/delete.html'

    # def delete_cart(self, session):
    #     data = {'id':''}
    #     session.get(self.url_cart)
    #     del_cart = session.post(self.url, data=data, headers=config.HEADERS)
    #     return del_cart



