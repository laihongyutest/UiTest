#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/4/9 16:26
# @Author  : laihongyu
# 主页元素
import allure

from Public.BaseFun import BaseFun


class MainPage(BaseFun):
    # 升级弹窗-关闭按钮
    close_update = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/update_cancle']"
    # 升级弹窗-升级按钮
    update = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/update_download_text']"
    # 首页顶部-左上角-koznak图标
    brand_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/update_download_text']"
    # 首页-左上角-搜索按钮
    search_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/iv_search']"
    # 首页-顶部-热词搜索按钮
    hot_word_search_icon = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/txt_hot_word']"
    # 首页-右上角-天气按钮
    weather_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/weather_icon']"
    # 首页-右上角-历史记录索按钮
    history_icon = "xpath", "//*[@resource-id='cn.wlantv.kznk:id/update_download_text']"
    # 首页-右上角-下载按钮
    download_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/download']"
    # 首页-右上角-分类按钮
    class_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/classification']"
    # 首页-右上角-游戏按钮
    fun_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/funIcon']"
    # 首页-右上角-直播按钮
    live_icon = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/zhiboTx']"
    # 首页-底部-个人中心按钮
    personal_center = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]'
    # 首页-底部-vip推荐页按钮
    vip_recommend = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]'
    # 首页-底部-热点页按钮
    hot = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]'
    # 首页-底部-主页按钮
    home = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]'
    # 首页- 模板9
    model9 = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/post']"
    # 首页 -开机弹窗广告关闭按钮
    run_adv_close = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/img_cancle']"
    # 开机弹窗广告
    run_adv_click = 'xpath', "//*[@resource-id='cn.wlantv.kznk:id/img_adv']"

    # 首页-分页巴扎
    ShouYeFenYe_BaZha = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.TextView'
    # 首页-分页电影
    ShouYeFenYe_Movie = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]'
    # 首页-分页电视剧
    ShouYeFenYe_Tv = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView'
    # 首页-分页动画
    ShouYeFenYe_DongMan = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView'
    # 首页-分页丝路
    ShouYeFenYe_SiLu = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.TextView'
    # 首页-分页主页
    ShouYeFenYe_Main = 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'

    # 浮窗关闭
    fubiao_close = 'xpath', 'cn.wlantv.kznk:id/close'
    # 浮窗点击
    fubiao_go = 'xpath', 'cn.wlantv.kznk:id/floatImg'

    # 输入登录账号
    @allure.step('点击个人中心页')
    def go_to_personal_center(self):
        self.click(self.personal_center)


if __name__ == "__main__":
    # MainPage().go_to_login_center()
    print(MainPage.personal_center)
