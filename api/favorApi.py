# -*- coding:utf-8 -*-

import config
from tools.logger import logger
log = logger().get_logger()

class Favor():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/goods/favor.html'

    log.info('favor')
    def favor(self, session):
        data = {
            "id": 1
        }
        resp = session.post(self.url, data=data, headers=config.HEADERS)
        return resp


