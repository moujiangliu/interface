# -*- coding:utf-8 -*-
import os

'''测试项目host'''
IP = 'http://121.42.15.146:9090/'

'''测试接口headers'''
HEADERS = {'X-Requested-With':'XMLHttpRequest'}

'''测试项目的工程目录路径'''
ABS_PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(ABS_PATH)

'''提交订单提取的jump_url'''
JUMP_URL = None

'''MYSQL数据库配置表'''
MYSQL_HOST = '192.168.56.101'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'mtx'
MYSQL_PORT = 3306

