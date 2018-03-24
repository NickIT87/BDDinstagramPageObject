#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.AllPagesConstructor import PageConstructor


class Reactivated(PageConstructor):
    # locators for this page
    URL = 'https://www.instagram.com/#reactivated'
    DOWNLOAD_LINK = (By.LINK_TEXT, 'Скачать приложение')
    NOT_NOW_LINK = (By.LINK_TEXT, 'Не сейчас')

    def downloadApp(self):
        pass

    def doNotDownloadTheApp(self):
        refuse_button = self.findElement(self.NOT_NOW_LINK)
        refuse_button.click()
