from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/driver/geckodriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框输入了“Buy peacock feathers”
        # 伊迪丝的爱好是使用假蝇做做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示了“1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was \n{0}".format(table.text)
        # )
        self.assertIn(
            "1: Buy peacock feathers", [row.text for row in rows],
            "New to-do item did not appear in table -- its text was \n{0}".format(table.text)
        )
        # 页面中有显示了一个文本框，可以输入其他的待办事项
        # 她输入了”Use peacock feathers to make a fly"
        # 伊迪丝做事很有调理
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，她的清单中显示了这两个待办事项
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn("2: Use peacock feathers to make a fly",
            [row.text for row in rows]
        )

        # 伊迪丝想知道这个网站是否会记住她的清单
        self.fail('Finish the test')
        # 她看到网站为她声称了一个唯一的URL
        # 而且网页中有一些文字解说了这个功能

        # 她访问了那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了

if __name__ == '__main__':
    # calling unittest.main() will do the right thing and collect all the
    # module’s test cases for you, and then execute them.
    unittest.main()
