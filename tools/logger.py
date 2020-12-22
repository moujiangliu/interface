# -*- coding:utf-8 -*-

import logging.handlers
from tools.units import get_path
import time


class logger():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger('interface')
            # 给日志器设置总的级别,级别是封装在logging里面(日志level需要大写:DEBUG,INFO,WARNING,ERROR,CRITICAL)
            cls.logger.setLevel(logging.INFO)
            # 设置要输出的格式
            # fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)s)] - %(message)s'
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)s)] ===> %(message)s"
            # 获取格式器
            ft = logging.Formatter(fmt)
            # 获取处理器
            tf = logging.handlers.TimedRotatingFileHandler(filename=get_path('logger', 'test.log'),
                                                      when='midnight',
                                                      interval=1,
                                                      backupCount=3,
                                                      encoding='utf-8')
            # 在处理器中添加格式器
            tf.setFormatter(ft)
            cls.logger.addHandler(tf)

        return cls.logger


'''
class logger():
    def __init__(self):
        # 获取日志器
        self.logger = logging.getLogger('interface')
        # 设置要输出的log格式
        self.fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] ===> %(message)s"
        # 捕获log存放的文件夹
        self.filedir = get_path('logger', 'test.log')
        self.log_config()

    def log_config(self):
        if not self.logger.handlers:
            logging.basicConfig(level=logging.DEBUG,
                                format=self.fmt,
                                datefmt='%Y-%m-%d_%H:%M:%S',
                                filename=self.filedir,
                                filemode='w')
            # 打印的方式
            console = logging.StreamHandler()
            # 设置级别
            console.setLevel(logging.DEBUG)
            # 在处理器中添加格式器
            formatter = logging.Formatter(self.fmt)
            console.setFormatter(formatter)
            # 日志器中添加处理器
            self.logger.addHandler(console)

    def info(self,msg):
            self.logger.info(str(msg))

    def error(self,msg):
            self.logger.error(str(msg))

    def waring(self,msg):
        self.logger.warning(str(msg))
'''


if __name__ == '__main__':
    log = logger().get_logger()
    log.info('这是info级别的信息')









