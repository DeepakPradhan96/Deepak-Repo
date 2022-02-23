import unittest
from selenium import webdriver

class serchengine(unittest.TestCase):
    def Test(self):
        self.driver=webdriver.Firefox()
        self.driver.get('https://www.google.com/')
        print(self.driver.title)



    def Test2(self):
        self.driver=webdriver.firefox()
        self.driver.get('https://www.bing.com/')
        print(self.driver.title)


if __name__== '__main__':
    unittest.main()
