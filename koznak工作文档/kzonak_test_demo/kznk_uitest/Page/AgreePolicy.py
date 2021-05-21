#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/14 15:37
# @Author  : laihongyu
import allure

from Public.BaseFun import BaseFun


class AgreePolicy(BaseFun):
    # 同意协议按钮
    Agree = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/user_agree']"
    DisAgree = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/user_disagree']"

    @allure.step("首次打开app允许进入")
    def agree_click(self):
        self.click(self.Agree)

    @allure.step("首次打开app不允许进入")
    def disagree_click(self):
        self.click(self.DisAgree)


if __name__ == "__main__":
    AgreePolicy().agree_click()
