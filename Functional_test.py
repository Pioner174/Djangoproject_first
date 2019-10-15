from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''тест нового посетитиля'''
    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()
    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получитьл его позже'''
        self.browser.get('http://localhost:8000/')
        self.assertIn('To-DO', self.browser.title)
        self.fail('Закончить тест')
    

if __name__=='__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox()
# assert 'To-Do' in browser.title
# # удовлетворённая она снова ложится спать
# browser.quit()


