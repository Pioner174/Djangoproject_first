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

    
   
