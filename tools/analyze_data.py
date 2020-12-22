# -*- coding:utf-8 -*-

import yaml
from tools.units import get_path
import config

def analyze_data(filename,key):
    '''
    解析yml,得到一个列表嵌套字典的数据格式
    :param filename: login_data.yml
    :param key: test_login
    :return:
    '''
    # '../data/%s.yml %filename'
    # config.DIR_PATH + '/data/%s.yml %filename'
    with open(get_path('data',f'{filename}.yml'), 'r', encoding='utf-8') as f:
        data_list = []
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        pre_value = yaml_data.get(key)
        data = pre_value.values()
        # print(f'{data}的值是:')
        for value in data:
            data_list.append(value)
        # 第二种方法：extand
        # data_list.extend(data)
        return data_list
        # 构造数据---列表套字典
        # [{'accounts':'', 'pwd':'', 'expect':''},{'accounts':'', 'pwd':'', 'expect':''}]


if __name__ == '__main__':
    print(analyze_data('login_data', 'test_login'))


























