from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item



class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        '''ТЕСТ: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        '''тест: сохраняет элементы только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        '''Тест: сохранения POST запроса'''
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        '''тест: переадресует после POST запроса'''
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(responce.status_code, 302)
        self.assertEqual(responce['location'], '/')

    def test_displays_all_list_items(self):
        '''тест: отражаются все элементы списка'''
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        responce = self.client.get('/')

        self.assertIn('itemey 1', responce.content.decode())
        self.assertIn('itemey 2', responce.content.decode())

class ItemModelTest(TestCase) :
    '''Тест модели элемента списка'''

    def test_saving_and_retrieving_items(self):
        '''тест сохранения и получения элементов списка'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
