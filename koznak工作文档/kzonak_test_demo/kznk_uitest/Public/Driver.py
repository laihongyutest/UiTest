#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/2/26 17:15
# @Author  : laihongyu
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Public.ReadFile import ReadFile


class ReturnDriver:
    def __init__(self):
        desired_list = ReadFile().read_yaml()
        self.desired_caps = {}
        self.desired_caps['platformName'] = desired_list['platformName']
        self.desired_caps['platformVersion'] = desired_list['platformVersion']
        self.desired_caps['deviceName'] = desired_list['deviceName']
        self.desired_caps['appPackage'] = desired_list['appPackage']
        self.desired_caps['appActivity'] = desired_list['appActivity']
        self.desired_caps['noReset'] = desired_list['noReset']
        self.desired_caps['automationName'] = desired_list['automationName']

    def appium_desired(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return driver


if __name__ == "__main__":
    test = ReturnDriver().appium_desired()
    # 跳过广告
    WebDriverWait(test, 30).until(lambda x: x.find_element_by_id('cn.wlantv.kznk:id/txt_time'))
    test.find_element_by_id('cn.wlantv.kznk:id/txt_time').click()
    # 开机弹窗广告
    WebDriverWait(test, 30).until(lambda x: x.find_element(By.ID, 'cn.wlantv.kznk:id/img_cancle'))
    test.find_element_by_id('cn.wlantv.kznk:id/img_cancle').click()
    # 首页轮播大图
    WebDriverWait(test, 30).until(lambda x: x.find_element(By.ID, 'cn.wlantv.kznk:id/layout_img'))
    test.find_element_by_id('cn.wlantv.kznk:id/layout_img').click()
    res = test.find_elements_by_id('cn.wlantv.kznk:id/post')
    print(res, len(res))
