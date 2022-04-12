from selenium import webdriver
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
        self.assertIn('To-Do',self.browser.title),"Browser title was :"+self.browser.title
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
