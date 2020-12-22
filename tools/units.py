# -*- coding:utf-8 -*-

import os
from os.path import abspath, dirname, join, realpath, pardir

def get_path(*args):
    ROOT_PATH = abspath(join(dirname(realpath(__file__)), pardir))
    fp_path = ROOT_PATH
    for item in args:
        fp_path = os.path.join(fp_path, item)
    return fp_path


if __name__ == '__main__':
    print(get_path('data', 'log_data.yml'))