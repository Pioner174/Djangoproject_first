from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    '''Текст на токсичность'''

    def test_bad_maths(self):
        self.assertEqual(1+1,3)
