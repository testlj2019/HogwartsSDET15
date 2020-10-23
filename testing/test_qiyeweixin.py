# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # cookies = self.driver.get_cookies()
        # print(cookies)
        #

        # 存储cookie
        # db = shelve.open('cookies')
        # db['cookies'] = cookies
        # db.close()

        db = shelve.open('cookies')
        cookies = db['cookies']
        db.close()
        # print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys('G:\Test\HogwartsSDET15\data\\testData2.xls')
        sleep(3)
