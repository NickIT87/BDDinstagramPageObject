#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import time
import unittest
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

class PageConstructor(unittest.TestCase):
    #initialize webdriver and inherit metods from unittest
    def __init__(self, driver):
        super(PageConstructor, self).__init__()
        self.driver = driver
    #global method - find and return element if this element is visible
    def findVisibleElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located(locator))
        return element
    #global method - find and return element if this element is present in DOM
    def findElement(self, locator):
        element = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located(locator))
        return element
    #global method - find and return list of elements if this elements is present in DOM
    def findElems(self, locator):
        elements = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_all_elements_located(locator))
        return elements
    #global method - Check text present in element
    def checkTextPresentInElem(self, locator, text):
        WebDriverWait(self.driver,10).\
            until(expected_conditions.text_to_be_present_in_element(locator, text))
    # global method - Check element to be enabled
    def checkElementToBeClickable(self, locator):
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.element_to_be_clickable(locator))

    def clickViaScript(self, element):
        """
        Метод осуществляет клик по элементу через JS скрипт
        :param element: экземпляр класса WebElement
        """
        self.driver.execute_script("arguments[0].click();", element)