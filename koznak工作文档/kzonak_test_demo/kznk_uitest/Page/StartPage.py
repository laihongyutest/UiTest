#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/9 11:11
# @Author  : laihongyu
# 启动页
import allure

from Public.BaseFun import BaseFun


class StartPage(BaseFun):
    skip_adv = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/txt_time']"
    adv_details = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/txt_go']"
    # 小米_授权弹窗 -点击
    xiaomi_auth = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView'
    # 小米始终允许
    XiaomiAllow = 'xpath', "//*[@resource-id='com.lbe.security.miui:id/permission_allow_button']"
    # 第二个按钮
    XiaomiAllow2 = 'xpath', "//*[@resource-id='com.lbe.security.miui:id/permission_allow_onetime_button']"

    @allure.step("首次打开始终允许操作")
    def xiaomi_allow_click(self):
        self.click(self.XiaomiAllow)
