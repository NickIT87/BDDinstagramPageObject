#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.AllPagesConstructor import PageConstructor
import pyautogui
import time

class PasswordReset(PageConstructor):
    # locators for this page
    USERNAME_INPUT = (By.ID, 'cppEmailOrUsername')
    SUBMIT_BTN = (By.XPATH, '//*[@id="react-root"]/section/main/div/article/form/div[3]/div/div/span/button')

    def putUserData(self, data):
        usr_name_input = self.findElement(self.USERNAME_INPUT)
        usr_name_input.send_keys(data)
        #time.sleep(2)

    def clickCaptcha(self):
        pyautogui.click(941, 467)
        time.sleep(2)

    def submitForm(self):
        #self.checkElementToBeClickable(self.SUBMIT_BTN)
        #btn = self.findElement(self.SUBMIT_BTN)
        #btn.click()
        pyautogui.click(991, 559)
        time.sleep(2)