# -*- coding:utf-8 -*-

import requests
from faker import Faker
from api.registerApi import RegisterApi
from tools.logger import logger
from tools.pymysqlutil import DataBaseHandle
log = logger().get_logger()

class TestRegister():
    def setup_class(self):
        self.session = requests.Session()
        # 实例化MYSQL接口
        self.db = DataBaseHandle()
        self.reg_obj = RegisterApi()

    def test_register(self):
        # 实例化faker这个类
        fake = Faker()

        # 对data数据进行构造
        username = fake.first_name()
        print(f'fake构造的用户名:{username}')
        password = fake.password()
        print(f'fake构造的密码:{password}')
        data = {
            'accounts': username,
            'pwd': password,
            'type': 'username',
            'is_agree_agreement': 1,
        }
        res = self.reg_obj.registerApi(self.session, data=data)
        re = res.json()
        # print('re的响应值是: ', re)
        # assert re['msg'] == '注册成功'

        # 进行一个断言：查询数据库，看一下刚才注册的数据是否成功存入到数据库中
        sql = f'SELECT pwd,username FROM s_user WHERE username = "{username}"'
        data = self.db.selectDb(sql)
        print('返回的数据是: ', data)
        assert data[0][1] == username



