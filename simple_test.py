from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def tesr_can_start_a_list_and_retrieve_it_later(self):
        self.assertIn(1,1)
        
    



calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(NewVisitorTest))
runner = unittest.TextTestRunner(verbosity=3)
runner.run(calcTestSuite)