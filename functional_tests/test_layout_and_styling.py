from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 伊迪丝访问网页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到输入框完美地居中显示
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # 她新建了一个清单，看到输入框仍完美地剧中显示
        inputbox.send_keys("testing\n")
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load():
            inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
