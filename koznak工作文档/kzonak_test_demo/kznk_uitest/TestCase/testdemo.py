#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/19 10:38
# @Author  : laihongyu
import random
import time
import uuid


def generate_gid():
    gids = []
    for number in range(100000, 10000000):
        gids.append(number)
    for gid in gids:
        index0 = random.randint(0, len(gids) - 1)
        index1 = len(gids) - 1
        tmp = gids[index0]
        gids[index0] = gids[index1]
        gids[index1] = tmp
    return gids.pop()


# print(time.strftime('%Y%m%d_%H%M%S'))
# print(uuid.uuid1())
l = []
while len(l) < 1000:
    l.append(uuid.uuid1())
print(l)
print(len(l))
print(len(set(l)))
# if len(l) != len(set(l)):
#     print('有重复')


def find_element(self, loc, timeout=60):
    mode, value = loc[0], loc[1]
    ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))
    return ele
    # try:
    #     if mode == "ID":
    #         # find_element(*loc)
    #         # 显示等待（等待特定元素出现
    #         # 隐式等待(等待所有元素),driver.implicitly_wait(3)
    #         # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((*loc))
    #         # element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
    #         WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements_by_id(value))
    #         return self.driver.find_elements_by_id(value)
    #     elif mode == "NAME":
    #         WebDriverWait(self.driver, timeout).until(lambda x: x.find_element_by_name(value))
    #         return self.driver.find_element_by_name(value)
    #     elif mode == "CLASS_NAME":
    #         WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(By.CLASS_NAME, value))
    #         return self.driver.find_element(By.CLASS_NAME, value)
    #     elif mode == "ACC_ID":
    #         WebDriverWait(self.driver, timeout).until(lambda x: x.find_element_by_accessibility_id(value))
    #         return self.driver.find_element_by_accessibility_id(value)
    #     elif mode == "XPATH":
    #         WebDriverWait(self.driver, timeout).until(lambda x: x.find_element_by_xpath(value))
    #         return self.driver.find_element_by_xpath(value)
    #     else:
    #         print("不存在获取元素方法")
    # except Exception as e:
    #     print('未找到元素,报错{}'.format(e))
    #     self.log.error("获取元素时失败,失败原因__{}__".format(e))

