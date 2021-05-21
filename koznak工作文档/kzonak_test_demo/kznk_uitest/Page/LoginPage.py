#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/13 10:00
# @Author  : laihongyu
import allure

from Public.BaseFun import BaseFun


class LoginPage(BaseFun):
    # 关闭半屏-登录弹窗
    Close = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/iv_close']"
    # 验证码登录-输入电话
    InputTel = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/et_telephone']"
    # 获取验证码
    GetVerCode = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/txt_validation']"
    # 验证码输入框
    DavidVerCode = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/txt_validation']"
    # 登录按钮
    LoginButton = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/bt_login']"
    # 切换登录
    ChgToPwdLogin = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/password_login']"
    # 密码登录-输入密码
    InputPwd = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/et_password']"
    # FullScreen登录
    ForgetPwd = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/forget_psw']"
    # 修改密码 -确定按钮
    DecChgPwd = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/bt_reset_password']"
    # 勾选协议
    CheckProtocol = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/check']"
    # 退出-登录页
    BackButton = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/iv_back']"
    # 用户协议
    Agreement = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/agreement']"
    # 《隐私政策》
    Policy = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/policy']"
    # 切换账号
    ChangeAccount = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/top_register']"
    # 登录/注册按钮
    LoginSignButton = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/loginBt']"

    @allure.step("个人中心-登录/注册按钮")
    def login_click(self):
        self.click(self.LoginSignButton)

    # '点击账号输入区域'
    @allure.step('点击账号输入区域')
    def click_tel(self):
        self.click(self.InputTel)

    # 点击输入密码区域
    @allure.step('点击密码输入区域')
    def click_pwd(self):
        self.click(self.InputPwd)

    # 输入登录账号
    @allure.step('输入登录账号')
    def input_tel(self, tel):
        self.send_keys(self.InputTel, tel)

    # 点击生成验证码
    @allure.step('点击生成验证码')
    def product_code(self):
        self.click(self.GetVerCode)

    # 输入验证码
    @allure.step('输入验证码')
    def input_code(self, code):
        self.send_keys(self.DavidVerCode, code)

    # 点击登录按钮
    @allure.step('点击登录按钮')
    def login(self):
        self.click(self.LoginButton)

    # 切换登录方式
    @allure.step('去密码登录页')
    def chg_to_pwd_login(self):
        self.click(self.ChgToPwdLogin)

    @allure.step('输入密码')
    def input_pwd(self, pwd):
        self.send_keys(self.InputPwd, pwd)


if __name__ == "__main__":
    test = LoginPage().login_click()
