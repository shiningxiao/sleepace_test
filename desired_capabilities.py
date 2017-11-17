#!/usr/bin/env python
import os
from time import strftime,gmtime,localtime

def get_desired_capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    # 华为：BY3ADH1515039155 moto：TA00402J6D
    desired_caps['deviceName'] = 'BY3ADH1515039155'#经验证没有关系，但必须要有
    desired_caps['appPackage'] = 'com.medicatech.sleepace'#启动的应用的包名
    desired_caps['appActivity'] = 'com.medica.xiangshui.splash.activities.SplashActivity'  # 启动时的Activity
    # 使用unicodeKeyboard的编码方式来发送字符串
    desired_caps['unicodeKeyboard'] = True
    # 将键盘给隐藏起来
    desired_caps['resetKeyboard'] = True

    return desired_caps

def get_uri():
  return "http://localhost:4723/wd/hub"


def get_deviceinformation():
    pwd = os.getcwd()
    father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")#当前路径的父路径
    image_path = father_path + '\Image_new'
    now_time = strftime("%Y%m%d%H%M", localtime())#获取当前时间，输出格式：2016-07-211147注意gmtime（）换算的是0时区的时间
    device_info = {
        "deviceName":  "nexus6",
        "deviceVersion":  "7.1.1",
        "deviceLanguage": 'zh-cn',
        "Image_path": image_path,
        "now_time": now_time
    }
    return device_info