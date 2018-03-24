#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.AllPagesConstructor import PageConstructor


class Authorization(PageConstructor):
    # locators for this page
    URL = 'https://www.instagram.com/'
    LOGIN_LINK = (By.LINK_TEXT, 'Вход')
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.TAG_NAME, 'button') # the login button has no locator, but it is the only one
    LOGIN_ERROR_ALERT = (By.ID, 'slfErrorAlert')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Забыли пароль?')

    def login(self, username, password):
        login_link = self.findVisibleElement(self.LOGIN_LINK)
        login_link.click();
        username_field = self.findElement(self.USERNAME_INPUT)
        username_field.send_keys(username)
        password_field = self.findElement(self.PASSWORD_INPUT)
        password_field.send_keys(password)
        login_btn = self.findVisibleElement(self.LOGIN_BUTTON)
        login_btn.click()

    def registration(self):
        pass

    def checkErrorMsg(self, error_message):
        self.findVisibleElement(self.LOGIN_ERROR_ALERT)
        self.checkTextPresentInElem(self.LOGIN_ERROR_ALERT, error_message)

    def forgotPassword(self):
        self.findVisibleElement(self.LOGIN_LINK).click()
        self.findElement(self.FORGOT_PASSWORD_LINK).click()