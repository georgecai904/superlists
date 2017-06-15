from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):


    def setUp(self):
        self._driver_path = '/driver/geckodriver'
        self.browser = webdriver.Firefox(executable_path=self._driver_path)
        self.browser.implicitly_wait(3)
        # STAGING_SERVER = 'staging.artshub.xyz'
        # self.live_server_url = 'http://' + STAGING_SERVER
        print(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = self.browser.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])
