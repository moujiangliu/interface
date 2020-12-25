# -*- coding:utf-8 -*-

import config
from tools.logger import logger
log = logger().get_logger()

class Cancel():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/goods/favor.html'

    log.info('取消收藏api')
    def cancel(self, session):
        data = {
            "id": 1
        }
        resp = session.post(self.url, data=data, headers=config.HEADERS)
        return resp


