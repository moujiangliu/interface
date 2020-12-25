# -*- coding:utf-8 -*-

import requests
import allure
from api.favorApi import Favor
from api.loginApi import MtxLogin


class TestFavor():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口对象
        self.favor_api = Favor()
        # 调用成功的登录的接口
        MtxLogin().login_success(self.session)

    @allure.feature('收藏接口测试用例')
    @allure.title('收藏测试')
    @allure.description('收藏的接口测试用例')
    @allure.severity('normal')
    def test_favor(self):
        resp_favor = self.favor_api.favor(self.session)
        assert resp_favor.json().get("msg") == "收藏成功"

