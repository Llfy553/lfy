# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 11:16
# @Author  : Nancy
# @Email   : NancyWangDL@163.com
# @File    : TestCaseBaidu.py
# @Software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest

import unittest  # 导入测试用例的模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class baiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()

    def test_baiduSearch(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")

        time.sleep(3)

        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.quit()


# 函数入口，固定写法
if __name__ == "__main__":
    unittest.main()