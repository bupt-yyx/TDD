from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_reetrieve_it_later(self):
        #Edith has heaed about a cool new online to-do app.She goes
        #
        self.browser.get('http://localhost:8000')
        #
        self.assertIn('To-Do',self.browser.title)
        header_test=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_test)

        #she is invited to enter a to-do item straight way
        inputbox=self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(
            '1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',[row.text for row in rows]
        )
        #
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
