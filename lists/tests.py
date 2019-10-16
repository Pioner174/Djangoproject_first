from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string



class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        '''ТЕСТ: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    def test_can_save_a_POST_request(self):
        '''Тест: сохранения POST запроса'''
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', responce.content.decode())
        self.assertTemplateUsed(responce, 'home.html')
   
