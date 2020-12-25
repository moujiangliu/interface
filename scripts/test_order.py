# -*- coding:utf-8 -*-

import requests
from api.orderApi import Order
from api.loginApi import MtxLogin
import allure

class TestOrder():
    def setup_class(self):
        # web ui自动化 相当于创建driver
        # 初始化操作---前置条件--每天测试用例之前要进行的操作
        self.session = requests.Session()
        self.order_obj = Order()
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)

    @allure.feature('提交订单接口')
    @allure.description('提交订单的接口测试用例')
    @allure.severity('critical')
    @allure.title('提交订单')
    def test_order_success_case003(self):
        '''
        1. 依赖于登录: 登录测试用例级别(test_mtx_login)
        2. 依赖于登录: api接口级别的请求,完全独立
        依赖于登录
        :return:
        '''
        # 调用成功的登录接口
        # MtxLogin().login_success(self.session)
        resp_order = self.order_obj.order(self.session)
        assert resp_order.json().get('msg') == "提交成功"

    @allure.feature('提交订单接口2')
    @allure.description('提交订单的接口测试用例2')
    @allure.severity('normal')
    @allure.title('提交订单')
    def test_order_error(self):
        '''调用成功登陆的用例,需要放到setup_class里面,方便多个用例调用'''
        # 调用成功的登录接口
        # MtxLogin().login_success(self.session)
        pass
