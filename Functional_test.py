from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        '''тест: можно начать список и получитьл его позже!!!!'''
        self.browser.get('http://localhost:8000/')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows),
            f"Новый элемент списка не появился в таблице. Содержимое было :\n{table.text}"
        )
        self.fail('Закончить тест')


if __name__=='__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox()
# assert 'To-Do' in browser.title
# # удовлетворённая она снова ложится спать
# browser.quit()


