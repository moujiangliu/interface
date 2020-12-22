# -*- coding:utf-8 -*-

import pymysql
import config

class DataBaseHandle(object):
    '''定义MYSQL数据库操作类'''
    def __init__(self):
        '''
        定义实例方法共用的属性
        建立MYSQL连接
        '''
        self.ip = '192.168.56.101'
        self.username = 'root'
        self.password = '123456'
        self.database = 'mtx'
        self.port = 3306

        # 建立MYSQL连接
        self.db = pymysql.connect(host=config.MYSQL_HOST,
                        user=config.MYSQL_USERNAME,
                        password=config.MYSQL_PASSWORD,
                        database=config.MYSQL_DATABASE,
                        port=config.MYSQL_PORT)

        # self.db = pymysql.connect(self.ip, self.username, self.password, self.database, self.port)

    def insertDb(self, sql):
        '''插入数据
        insert into s_user(username,pwd) values('bull',123456)
        '''
        # 建立一个"cursor游标"对象,操作数据库
        self.cur = self.db.cursor()
        # 写sql语句容易出现问题,所以用try...except...finally进行捕获
        try:
            # 执行sql语句,用游标进行查询---返回结果---把结果保存在游标里面
            self.cur.execute(sql)
            # 对数据进行
            self.db.commit()
        except Exception as err:
            print('insert data err: ', err)
            self.db.rollback()   # 发生错误时回滚
        finally:
            self.cur.close()

    def deleteDb(self, sql):
        '''删除数据
        delete from s_user where username="mixuhui"
        '''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行删除语句
            self.cur.execute(sql)
            # 对语句进行提交
            self.db.commit()
        except Exception as err:
            print('delete data err: ', err)
            self.db.rollback()   # 发生错误时回滚
        finally:
            self.cur.close()

    def updateDb(self, sql):
        '''修改数据 sql
        update s_user set name="yaoyao" where name="shamo"
        '''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行更新语句
            self.cur.execute(sql)
            self.db.commit()
        except Exception as err:
            print('update data err: ', err)
            self.db.rollback()
        finally:
            self.cur.close()

    def selectDb(self, sql):
        '''查询数据
        sql语句就是正常的mysql语句,原生的sql
        select username, pwd from s_user where username = "shamo"
        '''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行插入语句
            self.cur.execute(sql)
            # 从游标里面取出全部的数据,赋值给一个变量
            self.data = self.cur.fetchall()
            return self.data
        except Exception as err:
            print('select data err: ', err)
            raise err
        finally:
            # 把游标关闭
            self.cur.close()

    def closeDB(self):
        '''关闭MYSQL数据库连接'''
        self.db.close()

'''第二种方法'''
# def op_mysql(sql):
#     db = pymysql.connect(host=config.MYSQL_HOST,
#                     user=config.MYSQL_USERNAME,
#                     password=config.MYSQL_PASSWORD,
#                     database=config.MYSQL_DATABASE,
#                     port=config.MYSQL_PORT
#
#     )
#     cur = db.cursor(cursor=pymysql.cursors.DictCursor)
#     # 判断是否需要commit、rollback, 根据select,updata,insert,delete的类型
#     cur.execute(sql)
#     sql_start = sql[:6].upper()
#     if sql_start == "SELECT":
#         resp = cur.fetchall()
#     else:
#         db.commit()
#         # db.rollback()
#         res = "ok"
#     cur.close()
#     db.close()
#     return resp


if __name__ == '__main__':
    db = DataBaseHandle()
    # 从s_user数据库表中查询username="shaomo"的username,pwd
    # data = db.selectDb('select id, salt, username, pwd from s_user where username = "Kelly" ')
    # data = db.selectDb('select id, salt, username, pwd from s_user')

    # data = db.updateDb('update s_user set username="moujiang" where username="shamo"')

    # data = db.insertDb('insert into s_user(username,pwd) values("moujiang003","moujiang003")')
    data = db.deleteDb('delete from s_user where username="moujiang003"')
    print(data)

    

