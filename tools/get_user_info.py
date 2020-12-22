# -*- coding:utf-8 -*-

from faker import Faker
import random
import config

def get_user_info(count):
    '''
    获取用户信息
    :return:
    '''
    # fake = Faker(locale='zh_CN')
    fake = Faker()
    data_list = []
    for i in range(1, count+1):
       data_dict = {}
       username = fake.first_name()
       password = fake.password()
       gender = random.randint(0,1)
       mobile = fake.phone_number()
       email = fake.email()
       address = fake.address()
       id_card = fake.ssn()
       data_dict['username'] = username
       data_dict['password'] = password
       # data_dict['gender'] = gender
       # data_dict['mobile'] = mobile
       # data_dict['email'] = email
       # data_dict['address'] = address
       # data_dict['id_card'] = id_card

       data_list.append(data_dict)

    return data_list


if __name__ == '__main__':
    userinfo = get_user_info(1)
    print(userinfo[0].get('username'))


