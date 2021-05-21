#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/13 18:22
# @Author  : LaiHongYu
# import time
import os

import allure
import pytest
from Page.LoginPage import LoginPage
# from Page.MainPage import MainPage
from Page.MainPage import MainPage
from Public.BaseFun import BaseFun, StartDriver

from Public.Driver import ReturnDriver


class TestLogin:

    def setup_class(self):
        self.driver = StartDriver()
        self.base = BaseFun(self.driver)
        self.login = LoginPage(self.driver)
        self.mape = MainPage(self.driver)

    #
    def test001(self):
        self.mape.go_to_personal_center()
        self.login.login_click()
        self.login.chg_to_pwd_login()
        self.login.click_tel()
        self.login.input_tel("18244211570")
        self.login.click_pwd()
        self.login.input_pwd("123456")
        self.login.login()


if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir=../Report", "TestLogin.py"])
    split = 'allure ' + 'generate  ' + '../Report ' + '-o ' + '../Report/html ' + '--clean'
    os.system(split)
