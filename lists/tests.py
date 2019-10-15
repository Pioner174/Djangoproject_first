from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest




class HomePageTest(TestCase):
    def test_root_url(self):
        '''ТЕСТ преобразования url в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_return(self):
        '''ТЕСТ: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))