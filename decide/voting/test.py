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
        
class TestListAndSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test(self):
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/admin/")
        self.driver.find_element_by_id("id_username").send_keys("decide")
        self.driver.find_element_by_id("id_password").send_keys("passdecide")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/voting/")
        self.driver.find_element_by_name("campo").click()
        self.driver.find_element_by_name("campo").send_keys("p")
        self.driver.find_element_by_css_selector(".btn-outline-success").click()
        self.assertTrue(len(self.driver.find_elements_by_class_name('table'))==1)
    def tearDown(self):
        self.driver.quit

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
  
    def test_testCreate(self):
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/admin/")
        self.driver.find_element_by_id("id_username").send_keys("decide")
        self.driver.find_element_by_id("id_password").send_keys("passdecide")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/voting/")
        self.driver.find_element_by_link_text("Create voting").click()
        self.driver.find_element_by_id("id_name").click()
        self.driver.find_element_by_id("id_name").send_keys("test1")
        self.driver.find_element_by_id("id_desc").click()
        self.driver.find_element_by_id("id_desc").send_keys("gygygygy")
        self.driver.find_element_by_id("id_question").click()
        self.driver.find_element_by_xpath("//select[@id='id_question']//option[@value='1']").click()
        self.driver.find_element_by_xpath("//select[@id='id_auths']//option[@value='1']").click()
        self.driver.find_element_by_css_selector(".btn").click()
        self.assertTrue(self.driver.find_elements_by_class_name("card-header"))
    def tearDown(self):
        self.driver.quit

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
  
    def test_delete(self):
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/admin/")
        self.driver.find_element_by_id("id_username").send_keys("decide")
        self.driver.find_element_by_id("id_password").send_keys("passdecide")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/voting/")
        self.driver.find_element_by_css_selector("tr:nth-child(2) .btn-danger").click()
        self.driver.find_element_by_css_selector(".btn-danger").click()
        self.assertTrue(self.driver.find_elements_by_class_name("card-header"))
    def tearDown(self):
        self.driver.quit

class TestEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
  
    def test_edit(self):
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/admin/")
        self.driver.find_element_by_id("id_username").send_keys("decide")
        self.driver.find_element_by_id("id_password").send_keys("passdecide")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get("http://decide-zapdos-votacion.herokuapp.com/voting/")
        self.driver.find_element_by_css_selector("tr:nth-child(1) .btn-warning").click()
        self.driver.find_element_by_id("id_name").click()
        self.driver.find_element_by_id("id_name").send_keys("pp")
        self.driver.find_element_by_css_selector(".btn").click()
        self.assertTrue(self.driver.find_elements_by_class_name("card-header"))
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
   
