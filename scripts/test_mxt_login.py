# -*- coding:utf-8 -*-
import pytest
import requests
from api.loginApi import MtxLogin
import allure
from tools.analyze_data import analyze_data

class TestLogin():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口对象
        self.login_api = MtxLogin()

    @allure.feature('登录接口正向用例测试')
    @allure.story('登录接口测试')
    @allure.title('正向登录')
    @allure.description('正向登录的接口测试,获取session')
    @allure.severity('critical')
    # 测试登录成功的测试用例
    def test_login_success_case001(self):
        resp_login = self.login_api.login_success(self.session)
        assert resp_login.json().get("msg") == "登录成功"

    # 参数化,用yaml文件去保存我们的测试数据
    @allure.feature('登录接口的参数化测试集合')
    @allure.story('登录接口的参数化测试')
    @allure.severity('critical')
    @allure.description('登录接口的参数化测试')
    @pytest.mark.parametrize('value', analyze_data('login_data', 'test_login'))
    @allure.title('登录的异常场景的参数化测试,测试数据是:{value}')
    def test_login_error_case002(self, value):
        data = {
            "accounts":value['accounts'],
            "pwd":value['pwd']
        }
        resp_login = self.login_api.login(self.session, data)
        assert resp_login.json().get('msg') == value['expect']






