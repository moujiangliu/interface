# -*- coding:utf-8 -*-

def pytest_collection_modifyitems(items):
    print("测试用例集合是: ", items)
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')
        item._nodeid = item.nodeid.encode().decode('unicode_escape')
