import unittest
from selenium import webdriver

class TestDeleteQuestion():
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit

    def test_deleteQuestion(self):
        self.driver.get("http://127.0.0.1:8000/admin/")
        self.driver.find_element_by_id('id_username').send_keys("decide")
        self.driver.find_element_by_id('id_password').send_keys("decide1234")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://127.0.0.1:8000/voting/question")
        self.driver.find_element_by_css_selector("tr:nth-child(1) .btn-danger").click()
        self.driver.find_element_by_css_selector(".btn-danger").click()

class TestCreateQuestion():
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit

    def test_createQuestion(self):
        self.driver.get("http://127.0.0.1:8000/admin/")
        self.driver.find_element_by_id('id_username').send_keys("decide")
        self.driver.find_element_by_id('id_password').send_keys("decide1234")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://127.0.0.1:8000/voting/question")
        self.driver.get("http://127.0.0.1:8000/admin/voting/question/add/")
        self.driver.find_element_by_id('id_desc').send_keys("Test selenium")
        self.driver.find_element_by_id('id_options-0-number').send_keys("1")
        self.driver.find_element_by_id('id_options-0-option').send_keys("SI")
        self.driver.find_element_by_id('id_options-1-number').send_keys("2")
        self.driver.find_element_by_id('id_options-1-option').send_keys("No")
        self.driver.find_element_by_class_name('default').click()


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        self.driver.get("http://127.0.0.1:8000/admin/")
        self.driver.find_element_by_id('id_username').send_keys("decide")
        self.driver.find_element_by_id('id_password').send_keys("decide1234")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://127.0.0.1:8000/voting/question")
        self.assertTrue(self.driver.find_element_by_class_name('card-header'))

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
