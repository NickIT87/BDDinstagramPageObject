#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
from pages.Authorization import Authorization
from pages.Reactivated import Reactivated
from pages.UserNewsFeed import UserNewsFeed
from pages.UserProfile import UserProfile
from pages.PasswordReset import PasswordReset

#_____________Global step - get resource url________
@Given('I am on authorization page')
def step_i_am_on_main_page(context):
    context.driver.maximize_window()
    context.driver.get(Authorization.URL)

#_____________Steps of login.feature________________
@Then('Login as {username}, {password}')
def step_login_into_resource(context, username, password):
    authorization_page = Authorization(context.driver)
    authorization_page.login(username, password)

@Then('Skip download app')
def step_skip_download_application(context):
    download_app_page = Reactivated(context.driver)
    download_app_page.doNotDownloadTheApp()

@When('The authorization as {username} complete, we check logout function')
def step_verify_user_page_and_logout(context, username):
    user_news_page = UserNewsFeed(context.driver)
    user_news_page.checkUserName(username)
    user_news_page.moveToProfile()
    user_profile_page = UserProfile(context.driver)
    user_profile_page.logout()

@When('The authorization fail, we can see {error_message}')
def step_check_login_error_msg(context, error_message):
    authorization_page = Authorization(context.driver)
    authorization_page.checkErrorMsg(error_message)

@Then('Click forgot password link')
def step_click_on_forgot_password_link(context):
    authorization_page = Authorization(context.driver)
    authorization_page.forgotPassword()

@Then('Put user {data}, click captcha, and submit the form')
def step_bypass_of_captcha(context, data):
    pass_reset_page = PasswordReset(context.driver)
    pass_reset_page.putUserData(data)
    pass_reset_page.clickCaptcha()
    pass_reset_page.submitForm()