#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.AllPagesConstructor import PageConstructor


class UserProfile(PageConstructor):
    # locators for this page
    SETTINGS_BUTTON = (By.CLASS_NAME, 'coreSpriteMobileNavSettings')
    LOGOUT_BUTTON = (By.XPATH, '/html/body/div[4]/div/div[2]/div/ul/li[4]/button')

    def logout(self):
        settings_btn = self.findElement(self.SETTINGS_BUTTON)
        settings_btn.click()
        logout_btn = self.findElement(self.LOGOUT_BUTTON)
        logout_btn.click()