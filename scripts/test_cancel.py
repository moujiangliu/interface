# -*- coding:utf-8 -*-

import requests
import allure
from api.cancelApi import Cancel
from api.favorApi import Favor
from api.loginApi import MtxLogin


class TestCancel():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化对象
        self.cancel_api = Cancel()
        # 调用成功登陆的接口
        MtxLogin().login_success(self.session)
        # 调用收藏成功的接口
        Favor().favor(self.session)

    @allure.feature('取消收藏接口')
    @allure.severity('normal')
    @allure.title('取消收藏')
    def test_cancel(self):
        resp = self.cancel_api.cancel(self.session)
        assert resp.json().get("msg") == "取消成功"
