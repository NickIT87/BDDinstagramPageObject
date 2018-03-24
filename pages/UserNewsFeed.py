#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.AllPagesConstructor import PageConstructor


class UserNewsFeed(PageConstructor):
    # locators for this page
    USERNAME_PROFILE_PAGE_LINK = (By.XPATH, '//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
    PROFILE_PAGE_LINK = (By.CLASS_NAME, 'coreSpriteDesktopNavProfile')

    def checkUserName(self, username):
        self.checkTextPresentInElem(self.USERNAME_PROFILE_PAGE_LINK, username)

    def moveToProfile(self):
        profile_link = self.findElement(self.PROFILE_PAGE_LINK)
        profile_link.click()
