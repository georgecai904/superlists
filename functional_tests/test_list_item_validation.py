from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from lists.models import Item, List
import time
import unittest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_duplicate_items(self):
        # 伊迪丝访问网页，新建了一个清单
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("First thing")
        inputbox.send_keys(Keys.RETURN)
        self.check_for_row_in_list_table("1: First thing")

        # 她不小心输入了一个重复的待办事项
        inputbox = self.get_item_input_box()
        inputbox.send_keys("First thing")
        inputbox.send_keys(Keys.RETURN)

        # 她看到一条有帮助的错误消息
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You're already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # 伊迪丝新建一个清单
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("First thing")
        inputbox.send_keys(Keys.RETURN)
        self.check_for_row_in_list_table("1: First thing")

        # 她不小心输入了一个重复的待办事项
        inputbox = self.get_item_input_box()
        inputbox.send_keys("First thing")
        inputbox.send_keys(Keys.RETURN)

        # 她看到一条有帮助的错误消息
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertTrue(error.is_displayed())

        # 为了消除错误，她开始在输入框中输入内容
        self.get_item_input_box().send_keys('a')

        # 看到错误消息消失了，她很高兴
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertFalse(error.is_displayed())
