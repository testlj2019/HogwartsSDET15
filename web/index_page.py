# !/usr/bin python
# -*- coding;utf-8 -*-
from selenium import webdriver
from login_page import LoginPage
from register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def goto_login(self):
        self.diver.fin
        return LoginPage(self.diver)

    def goto_register(self):
        return RegisterPage()






















        yo