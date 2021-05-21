#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/2/26 18:03
# @Author  : laihongyu
import threading

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Public.Log import Log
from Public.ReadFile import ReadFile
from conftest import DriverUtil


def StartDriver():
    desired_list = ReadFile().read_yaml()
    desired_caps = {}
    desired_caps['platformName'] = desired_list['platformName']
    desired_caps['platformVersion'] = desired_list['platformVersion']
    desired_caps['deviceName'] = desired_list['deviceName']
    desired_caps['appPackage'] = desired_list['appPackage']
    desired_caps['appActivity'] = desired_list['appActivity']
    desired_caps['noReset'] = desired_list['noReset']
    desired_caps['automationName'] = desired_list['automationName']

    driver_caps = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver_caps


class BaseFun:
    def __init__(self, driver):
        self.driver = driver
        self.log = Log()
        print(id(self.driver))

    def find_element(self, loc, timeout=60):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))
            return ele
        except Exception as e:
            self.log.error("获取元素时失败,失败原因__{}__".format(e))

    def clear(self, loc):
        self.find_element(loc).clear()

    def send_keys(self, loc, text):
        self.find_element(loc).send_keys(text)

    def click(self, loc):
        self.find_element(loc).click()

    def get_text(self, loc):
        return self.find_element(loc).text

    def maximizewindow(self):
        self.driver.maximize_window()

    def get_url(self, url):
        self.driver.get(url)

    def wait(self, sec):
        self.driver.implicitly_wait(sec)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    driver = StartDriver()
    test = BaseFun(driver)
    personal_center = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]'
    test.click(personal_center)
