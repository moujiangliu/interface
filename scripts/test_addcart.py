# -*- coding:utf-8 -*-

import requests
from api.addCartApi import AddCart
from api.deleteCartApi import DeleteCart
from api.loginApi import MtxLogin
import allure


class TestCart():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口api参数
        self.addcart_obj = AddCart()
        self.delcart_obj = DeleteCart()
        # 调用成功登陆的接口
        MtxLogin().login_success(self.session)

    @allure.feature('加入购物车接口')
    @allure.severity('critical')
    @allure.title('加入购物车')
    def test_addcart_success(self):
        '''
        加入购物车接口测试用例
        '''
        resp_cart = self.addcart_obj.add_cart(self.session)
        assert resp_cart.json().get("msg") == "加入成功"




