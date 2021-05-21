#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/13 10:49
# @Author  : laihongyu
import allure

from Public.BaseFun import BaseFun


class PersonalCenter(BaseFun):
    # 夜间模式按钮
    DarkModel = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/chk_dark']"
    # 夜间模式文字
    DarkModel2 = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/dark_txt']"
    # 消息按钮
    MessageButton = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/img_message']"
    #  设置按钮
    Setting = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/img_setting']"
    #  帮助中心
    HelpCenter = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_help_center']"
    HelpCenterBack = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/img_webview_back']"
    # 会员中心
    VipCenter = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_vip']"
    # 积分中心
    Points = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]'
    # 预约
    Appointment = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_make_an_appointment']"
    # 追剧
    BingeWatching = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_binge_watching']"
    # 下载
    Download = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_download']"
    # 收藏
    Collection = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_favorite']"
    # 卡包
    CardBag = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/ll_card_bag']"
    # 未登录头像和文字区域
    NotLoginImage = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/tv_not_login']"
    #
