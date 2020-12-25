# -*- coding:utf-8 -*-

import requests
import allure
from api.loginApi import MtxLogin
from api.orderApi import Order
from api.payOrderApi import PayOrder


class TestPayOrder():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化支付接口
        self.pay_obj = PayOrder()
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)

    @allure.feature('支付订单接口')
    @allure.severity('critical')
    @allure.title('支付订单')
    def test_payorder(self):
        '''
        支付订单接口测试
        '''
        # 调用成功的登录接口
        # MtxLogin().login_success(self.session)
        # 调用提交订单的接口---> 需要获取jump_url 数据提取 数据关联
        Order().order(self.session)
        # 请求支付接口
        resp_pay = self.pay_obj.pay_order(self.session)
        assert "支付成功" in resp_pay.text





