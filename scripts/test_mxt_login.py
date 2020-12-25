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

    @allure.feature('正向登录接口')
    @allure.severity('critical')
    @allure.title('正向登录')
    def test_login_success_case001(self):
        '''
        正向登录接口测试用例
        '''
        resp_login = self.login_api.login_success(self.session)
        assert resp_login.json().get("msg") == "登录成功"

    # 参数化,用yaml文件去保存我们的测试数据
    @allure.feature('登录接口的参数化测试集合')
    @allure.severity('critical')
    @pytest.mark.parametrize('value', analyze_data('login_data', 'test_login'))
    @allure.title('登录异常场景的参数化,测试数据是:{value}')
    def test_login_error_case002(self, value):
        '''
        登录接口参数化测试用例
        '''
        data = {
            "accounts":value['accounts'],
            "pwd":value['pwd']
        }
        resp_login = self.login_api.login(self.session, data)
        assert resp_login.json().get('msg') == value['expect']






