from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time
import unittest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空

        # 她输入一些文字，然后再次提交，这次没问题了

        # 她有点调皮，有提交了一个空待办事项

        # 输入文字后就没问题了
        self.fail('Write me!')
