#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/13 22:39
# @Author  : laihongyu
import threading

from Public.Driver import ReturnDriver


class DriverUtil(object):
    '''driver工具类'''

    __instance = None   # 定义一个类属性
    __instance_lock = threading.Lock()  # 加锁

    @classmethod
    def get_driver(cls):
        '''获取driver'''
        with DriverUtil.__instance_lock:
            if not DriverUtil.__instance:
                DriverUtil.__instance = ReturnDriver().appium_desired()
        return DriverUtil.__instance
1