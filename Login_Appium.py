# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
import time
import desired_capabilities

# 手机基本信息
device_info = desired_capabilities.get_deviceinformation()
deviceName = device_info['deviceName']
deviceVersion = device_info['deviceVersion']
deviceLanguage = device_info['deviceLanguage']
Image_path = device_info['Image_path']
nowTime = device_info['now_time']
print(deviceName, deviceVersion, deviceLanguage, Image_path, nowTime)


class SleepaceAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        self.driver = webdriver.Remote(uri, desired_caps)

    # 注册、首页相关
    def test_Login(self):
        # ######获取当前屏幕的分辨率（长和宽）#########
        devicesize = self.driver.get_window_size()
        y = devicesize['height']
        x = devicesize['width']

        time.sleep(20)
        self.driver.tap([(250, 166)], 100)# 关闭视频,需要修改，目前是点击的指定的左边，需要想办法拓展成通用的
        time.sleep(10)
        self.driver.get_screenshot_as_file(
            Image_path + '\Login\\' + deviceVersion + '_' + deviceName + '_' + deviceLanguage + '_' + nowTime + '.jpg')
        # 登陆
        self.driver.find_element_by_id('com.medicatech.sleepace:id/login_account').clear()# 清除已有的账号信息
        name = self.driver.find_element_by_id('com.medicatech.sleepace:id/login_account')
        name.click()
        name.send_keys('shinning@sleepace.net')
        psd = self.driver.find_element_by_id('com.medicatech.sleepace:id/login_password')
        psd.click()
        psd.send_keys('111111')
        self.driver.find_element_by_id('com.medicatech.sleepace:id/login').click()
        time.sleep(10)
        self.driver.reset()  # 重置应用(类似删除应用数据)


    def tearDown(self):
        try:
            self.driver.quit()
        except Exception:
            pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SleepaceAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)