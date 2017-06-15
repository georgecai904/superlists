from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time
import unittest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys(Keys.ENTER)

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.fail("Stop Here")
        # 她输入一些文字，然后再次提交，这次没问题了
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy milk")

        # 她有点调皮，有提交了一个空待办事项
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys(Keys.ENTER)

        # 输入文字后就没问题了
        with self.wait_for_page_load():
            inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Make tea")
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Make tea")
